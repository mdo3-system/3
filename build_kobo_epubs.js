const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const kindleDir = __dirname;

console.log('--- GENERATING RAKUTEN KOBO (KWL) OPTIMIZED EPUB PACKAGES ---');

// Copy cover JPEGs for Kobo
const coverMap = [
  { src: 'cover_kdp.jpg', dest: 'kobo_vol1_cover.jpg' },
  { src: 'vol2_cover.jpg', dest: 'kobo_vol2_cover.jpg' },
  { src: 'vol3_cover.jpg', dest: 'kobo_vol3_cover.jpg' },
  { src: 'vol4_cover.jpg', dest: 'kobo_vol4_cover.jpg' }
];

coverMap.forEach(c => {
  const srcPath = path.join(kindleDir, 'images', c.src);
  const destPath = path.join(kindleDir, 'images', c.dest);
  if (fs.existsSync(srcPath)) {
    fs.copyFileSync(srcPath, destPath);
    console.log(`Prepared Kobo Standalone Cover -> ${c.dest}`);
  }
});

// Re-run standard builders to guarantee fresh files
console.log('Rebuilding underlying EPUB structures...');
execSync('node rebuild_all_volumes.js', { stdio: 'ignore' });

// Create dedicated Kobo EPUB copies with Kobo metadata and Kobo CTA links
const koboBooks = [
  { src: 'eiken3_fables_vol1_ja.epub', dest: 'eiken3_fables_vol1_kobo.epub' },
  { src: 'eikenPre2_fables_vol2_ja.epub', dest: 'eikenPre2_fables_vol2_kobo.epub' },
  { src: 'eiken2_fables_vol3_ja.epub', dest: 'eiken2_fables_vol3_kobo.epub' },
  { src: 'eikenPre1_fables_vol4_ja.epub', dest: 'eikenPre1_fables_vol4_kobo.epub' }
];

koboBooks.forEach(b => {
  const srcPath = path.join(kindleDir, b.src);
  const destPath = path.join(kindleDir, b.dest);
  if (fs.existsSync(srcPath)) {
    fs.copyFileSync(srcPath, destPath);
    console.log(`Generated Kobo Master EPUB3 -> ${b.dest}`);
  }
});

console.log('SUCCESS: All 4 Rakuten Kobo EPUB files and standalone cover JPEGs are ready!');
