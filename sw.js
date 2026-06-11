// KRONA Analytics — Service Worker v2.0
const CACHE_NAME = 'krona-v2';
const OFFLINE_URL = './index.html';

// Arquivos essenciais para funcionamento offline
const PRECACHE = [
  './',                     // página inicial (index)
  './index.html',
  './manifest.json',
  './icons/icon-72.png',
  './icons/icon-96.png',
  './icons/icon-128.png',
  './icons/icon-144.png',
  './icons/icon-152.png',
  './icons/icon-192.png',
  './icons/icon-384.png',
  './icons/icon-512.png'
];

// Instalação: pré-cache dos arquivos essenciais
self.addEventListener('install', event => {
  console.log('[SW] Instalando...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('[SW] Pré-cacheando arquivos essenciais');
        return cache.addAll(PRECACHE);
      })
      .then(() => self.skipWaiting())
  );
});

// Ativação: limpa caches antigos e assume controle
self.addEventListener('activate', event => {
  console.log('[SW] Ativando e limpando caches antigos');
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => {
              console.log(`[SW] Removendo cache antigo: ${key}`);
              return caches.delete(key);
            })
      );
    }).then(() => self.clients.claim())
  );
});

// Estratégia de fetch: cache-first para assets estáticos, network-first para navegação
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  // Ignorar requisições não HTTP (chrome-extension, etc.)
  if (!request.url.startsWith('http')) return;

  // Navegação (páginas HTML): network-first com fallback para index.html
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then(response => {
          // Cache da resposta para futuras visitas offline
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(request, responseClone);
          });
          return response;
        })
        .catch(async () => {
          // Fallback: tenta servir o index.html do cache
          const cachedIndex = await caches.match(OFFLINE_URL);
          if (cachedIndex) return cachedIndex;
          return new Response('Você está offline. Conecte-se à internet para acessar o conteúdo.', {
            status: 503,
            statusText: 'Offline',
            headers: new Headers({ 'Content-Type': 'text/html' })
          });
        })
    );
    return;
  }

  // Requisições de API ou dados (evitar cache)
  if (url.pathname.includes('/api/') || url.pathname.includes('/wp-json/')) {
    event.respondWith(fetch(request));
    return;
  }

  // Assets estáticos (JS, CSS, imagens, fontes, áudios): cache-first
  event.respondWith(
    caches.match(request)
      .then(cached => {
        if (cached) {
          return cached;
        }
        return fetch(request).then(response => {
          // Só armazena respostas bem-sucedidas e não opacas
          if (!response || response.status !== 200 || response.type === 'opaque') {
            return response;
          }
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(request, responseClone);
          });
          return response;
        });
      })
      .catch(() => {
        // Fallback para recursos específicos, se necessário
        if (request.destination === 'audio') {
          // Áudio offline? retorna silêncio (opcional)
          return new Response(null, { status: 204 });
        }
        return new Response('Recurso não encontrado offline.', { status: 404 });
      })
  );
});

// Sincronização em segundo plano (para futuros envios de dados)
self.addEventListener('sync', event => {
  if (event.tag === 'sync-progress') {
    console.log('[SW] Sincronizando progresso do usuário');
    // Aqui poderia ser implementada a sincronização com IndexedDB ou API
    event.waitUntil(syncProgress());
  }
});

async function syncProgress() {
  // Exemplo: recuperar dados do IndexedDB e enviar ao servidor
  console.log('[SW] Executando syncProgress...');
  // Implementação futura
}

// Notificações push (reservado)
self.addEventListener('push', event => {
  const data = event.data ? event.data.json() : {};
  const title = data.title || 'KRONA Analytics';
  const options = {
    body: data.body || 'Novo conteúdo disponível!',
    icon: './icons/icon-192.png',
    badge: './icons/icon-96.png',
    vibrate: [200, 100, 200],
    data: { url: data.url || './' }
  };
  event.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener('notificationclick', event => {
  event.notification.close();
  const url = event.notification.data?.url || './';
  event.waitUntil(
    clients.openWindow(url)
  );
});
