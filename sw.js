// KRONA Analytics — Service Worker v1.0 (caminhos relativos)
const CACHE_NAME = 'krona-v1';

// Arquivos essenciais para funcionar offline (usando caminhos relativos ao diretório do app)
const PRECACHE = [
  './',                     // página inicial (o próprio diretório)
  './index.html',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png'
];

// INSTALL: pré-cachear arquivos essenciais
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(PRECACHE))
      .then(() => self.skipWaiting())
  );
});

// ACTIVATE: limpar caches antigos
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys
          .filter(key => key !== CACHE_NAME)
          .map(key => caches.delete(key))
      )
    ).then(() => self.clients.claim())
  );
});

// FETCH: Cache-first para assets, network-first para navegação
self.addEventListener('fetch', event => {
  const { request } = event;

  // Ignorar requisições não-HTTP (ex: chrome-extension)
  if (!request.url.startsWith('http')) return;

  // Navegação (HTML): network-first com fallback para o index.html do cache
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then(response => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, clone));
          return response;
        })
        .catch(() => caches.match('./index.html'))   // ← caminho relativo
    );
    return;
  }

  // Assets (CSS, JS, imagens): cache-first
  event.respondWith(
    caches.match(request).then(cached => {
      if (cached) return cached;
      return fetch(request).then(response => {
        if (!response || response.status !== 200 || response.type === 'opaque') {
          return response;
        }
        const clone = response.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(request, clone));
        return response;
      });
    })
  );
});

// BACKGROUND SYNC (reservado)
self.addEventListener('sync', event => {
  if (event.tag === 'sync-progress') {
    console.log('[SW] Background sync: sync-progress');
  }
});
