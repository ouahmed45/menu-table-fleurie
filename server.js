// La Table Fleurie – Menu Digital par QR Code
const http = require('http'), fs = require('fs'), path = require('path');

const PORT = process.env.PORT || 3000;
const MENU = JSON.parse(fs.readFileSync(path.join(__dirname, 'menu.json'), 'utf8'));
const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.jpg': 'image/jpeg',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json'
};

http.createServer((req, res) => {
  const url = new URL(req.url, 'http://x'), p = url.pathname;

  // API Menu
  if (p === '/api/menu') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'public, max-age=60' });
    return res.end(JSON.stringify(MENU));
  }

  // Fichiers statiques (pages, photos, icônes)
  let f = p === '/' ? '/index.html' : p;
  f = path.normalize(path.join(__dirname, 'public', f));
  if (!f.startsWith(path.join(__dirname, 'public'))) {
    res.writeHead(403);
    return res.end();
  }

  fs.readFile(f, (e, d) => {
    if (e) {
      res.writeHead(404);
      return res.end('Introuvable');
    }
    const ext = path.extname(f);
    res.writeHead(200, {
      'Content-Type': MIME[ext] || 'application/octet-stream',
      'Cache-Control': ext === '.jpg' || ext === '.png' ? 'public, max-age=604800' : 'no-cache'
    });
    res.end(d);
  });
}).listen(PORT, () => console.log(`La Table Fleurie (Menu Digital) : http://localhost:${PORT}`));

