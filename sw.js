/**
 * KRONA Analytics - Service Worker (sw.js)
 * Versão: 3.0
 * Estratégia de cacheamento para suporte offline completo.
 */

const CACHE_NAME = 'krona-analytics-v3';

// Ativos críticos pré-carregados durante a instalação
const PRECACHE_ASSETS = [
  './',
  './index.html', // Altere se o nome do seu arquivo principal for diferente
  'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js',
  'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap'
];

// Instalação do Service Worker e Pre-cache de recursos estáticos
self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(PRECACHE_ASSETS);
    }).catch(error => {
      console.warn('[Service Worker] Falha no pre-cache inicial:', error);
    })
  );
});

// Ativação do Service Worker e limpeza de caches antigos
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cache => {
          if (cache !== CACHE_NAME) {
            console.log('[Service Worker] Removendo cache antigo:', cache);
            return caches.delete(cache);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Interceptação de requisições (Estratégia: Stale-While-Revalidate)
// Garante carregamento instantâneo do cache enquanto busca atualizações em segundo plano
self.addEventListener('fetch', event => {
  // Ignora requisições que não sejam do tipo GET (como envio de PDFs por POST ou chamadas externas)
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.open(CACHE_NAME).then(cache => {
      return cache.match(event.request).then(cachedResponse => {
        const fetchPromise = fetch(event.request).then(networkResponse => {
          // Salva uma cópia atualizada no cache se o retorno da rede for válido
          if (networkResponse && networkResponse.status === 200) {
            cache.put(event.request, networkResponse.clone());
          }
          return networkResponse;
        }).catch(() => {
          // Silencia falhas de conexão para requisições que já estão no cache
        });

        // Retorna o cache se existir, caso contrário aguarda a rede
        return cachedResponse || fetchPromise;
      });
    })
  );
});
