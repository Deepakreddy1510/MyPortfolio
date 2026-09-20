import express from 'express';
import path from 'path';
import fs from 'fs';
import { execSync } from 'child_process';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;

const distDir = path.join(__dirname, 'dist');
const publicDir = path.join(__dirname, 'public');

// Ensure dist directory exists and is populated
function ensureBuild() {
  const needsBuild = !fs.existsSync(path.join(distDir, '404.html')) || !fs.existsSync(path.join(distDir, 'index.html'));
  if (needsBuild) {
    try {
      console.log('Generating static portfolio bundle...');
      execSync('python3 generate.py', { cwd: __dirname, stdio: 'inherit' });
    } catch (err) {
      console.error('generate.py execution error:', err);
      if (fs.existsSync(publicDir)) {
        fs.cpSync(publicDir, distDir, { recursive: true, force: true });
      }
    }
  }
}

ensureBuild();

// Serve static assets from dist folder
if (fs.existsSync(distDir)) {
  app.use(express.static(distDir, {
    extensions: ['html'],
    index: 'index.html'
  }));
}

// Fallback static middleware for public folder
if (fs.existsSync(publicDir)) {
  app.use(express.static(publicDir, {
    extensions: ['html'],
    index: 'index.html'
  }));
}

// Fallback 404 handler with safe error recovery
app.use((req, res) => {
  const dist404 = path.join(distDir, '404.html');
  const public404 = path.join(publicDir, '404.html');

  const fallbackHtml = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>404 - Page Not Found</title></head><body><h1>404 Not Found</h1><p>This page is not available.</p><a href="/">Back to portfolio</a></body></html>';

  if (fs.existsSync(dist404)) {
    res.status(404).sendFile(dist404, (err) => {
      if (err && !res.headersSent) {
        res.status(404).send(fallbackHtml);
      }
    });
  } else if (fs.existsSync(public404)) {
    res.status(404).sendFile(public404, (err) => {
      if (err && !res.headersSent) {
        res.status(404).send(fallbackHtml);
      }
    });
  } else {
    res.status(404).send(fallbackHtml);
  }
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on http://0.0.0.0:${PORT}`);
});
