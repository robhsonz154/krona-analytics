// KRONA Analytics — Service Worker v2.0 (caminhos absolutos otimizados)
const CACHE_NAME = 'krona-v2';

// Arquivos essenciais para funcionar offline de forma leve e rápida
const PRECACHE = [
  '/',
  '/index.html',
  '/manifest.json',
  '/icons/icon-192.png',
  '/icons/icon-512.png'
];

// INSTALL: pré-cachear arquivos essenciais
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(PRECACHE))
      .then(() => self.skipWaiting())
  );
});

// ACTIVATE: limpar caches antigos automaticamente
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

  // Ignorar requisições não-HTTP (ex: chrome-extension ou extensões de terceiros)
  if (!request.url.startsWith('http')) return;

  // Navegação (HTML): network-first com fallback offline seguro
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then(response => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, clone));
          return response;
        })
        .catch(() => caches.match('/index.html')) // ← corrigido para caminho absoluto seguro
    );
    return;
  }

  // Assets (CSS, JS, imagens): cache-first para máxima velocidade e leveza
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

// BACKGROUND SYNC (reservado para futuras atualizações de progresso do simulado)
self.addEventListener('sync', event => {
  if (event.tag === 'sync-progress') {
    console.log('[SW] Background sync: sync-progress');
  }
});


Em ter, 9 de jun de 2026 17:55, missoes <robhsonzrob342@gmail.com> escreveu:
{
  "name": "KRONA Analytics",
  "short_name": "KRONA",
  "description": "Simulado Técnico em Agronegócio — SENAR",
  "start_url": "/index.html",
  "scope": "/",
  "display": "standalone",
  "orientation": "portrait",
  "background_color": "#060A13",
  "theme_color": "#060A13",
  "lang": "pt-BR",
  "categories": ["education", "productivity"],
  "icons": [
    {
      "src": "/icons/icon-72.png",
      "sizes": "72x72",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-96.png",
      "sizes": "96x96",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-128.png",
      "sizes": "128x128",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-144.png",
      "sizes": "144x144",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-152.png",
      "sizes": "152x152",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "maskable"
    },
    {
      "src": "/icons/icon-384.png",
      "sizes": "384x384",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable"
    }
  ],
  "screenshots": [
    {
      "src": "/screenshots/screen1.png",
      "sizes": "390x844",
      "type": "image/png",
      "form_factor": "narrow",
      "label": "Tela inicial do KRONA Analytics"
    }
  ],
  "shortcuts": [
    {
      "name": "Iniciar Simulado",
      "short_name": "Simulado",
      "description": "Acesse os módulos do simulado",
      "url": "/index.html?shortcut=quiz",
      "icons": [{ "src": "/icons/icon-96.png", "sizes": "96x96" }]
    }
  ]
}
