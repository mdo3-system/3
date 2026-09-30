const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;
const zipBuildDir = path.join(kindleDir, 'vol2_kdp_zip_build');
const imagesZipDir = path.join(zipBuildDir, 'images');

try {
  if (fs.existsSync(zipBuildDir)) {
    fs.rmSync(zipBuildDir, { recursive: true, force: true });
  }
} catch (e) {}

fs.mkdirSync(zipBuildDir, { recursive: true });
fs.mkdirSync(imagesZipDir, { recursive: true });

const files = [
  'vol2_00_introduction.md',
  'vol2_chapter01_tortoise_and_hare.md',
  'vol2_chapter02_boy_who_cried_wolf.md',
  'vol2_chapter03_north_wind_and_sun.md',
  'vol2_chapter04_lion_and_mouse.md',
  'vol2_chapter05_ant_and_grasshopper.md',
  'vol2_chapter06_fox_and_grapes.md',
  'vol2_chapter07_town_mouse_country_mouse.md',
  'vol2_chapter08_crow_and_pitcher.md',
  'vol2_chapter09_dog_and_his_shadow.md',
  'vol2_chapter10_milkmaid_and_her_pail.md',
  'vol2_99_epilogue_and_next_volume.md'
];

// Extract ONLY images actually used in this volume
const usedImageSet = new Set(['vol2_cover.jpg', 'cover_kdp.jpg']);
files.forEach(f => {
  const mdPath = path.join(kindleDir, f);
  if (fs.existsSync(mdPath)) {
    const text = fs.readFileSync(mdPath, 'utf8');
    const matches = text.match(/images\/([^\s\)\"\'>]+)/g) || [];
    matches.forEach(m => usedImageSet.add(m.replace('images/', '')));
  }
});
const srcImagesDir = path.join(kindleDir, 'images');
const images = Array.from(usedImageSet).filter(img => fs.existsSync(path.join(srcImagesDir, img)));

images.forEach(img => {
  fs.copyFileSync(path.join(srcImagesDir, img), path.join(imagesZipDir, img));
});


function mdToHtml(md) {
  let html = md;
  html = html.replace(/<div style="page-break-before: always;"><\/div>/g, '');
  html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');
  html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
  html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');

  html = html.replace(/<img src="images\/(.*?)" alt="(.*?)" style=".*?" \/>/g, '<div class="center"><img src="images/$1" alt="$2" /></div>');
  html = html.replace(/!\[(.*?)\]\(images\/(.*?)\)/g, '<div class="center"><img src="images/$2" alt="$1" /></div>');

  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
  html = html.replace(/`(.*?)`/g, '<code>$1</code>');

  const lines = html.split('\n');
  let inTable = false;
  let newLines = [];
  let tableHeader = true;

  for (let line of lines) {
    if (line.trim().startsWith('|')) {
      if (!inTable) {
        inTable = true;
        tableHeader = true;
      }
      if (line.includes('---')) continue;
      const cells = line.split('|').filter((_, idx, arr) => idx > 0 && idx < arr.length - 1).map(c => c.trim());
      if (tableHeader) {
        tableHeader = false;
      } else if (cells.length >= 4) {
        const [scene, g4, g3, nuance] = cells;
        newLines.push(`
<div class="comparison-card" style="border: 1px solid #3498db; border-radius: 8px; padding: 12px 16px; margin: 18px 0; background-color: #f8f9fa;">
  <div style="font-weight: bold; color: #2c3e50; font-size: 1.05em; border-bottom: 1px solid #d6dbdf; padding-bottom: 6px; margin-bottom: 10px;">📌 場面：${scene}</div>
  <div style="margin-bottom: 8px; color: #444;"><strong style="color: #7f8c8d;">【Grade 3 基礎】</strong> ${g4}</div>
  <div style="margin-bottom: 10px; color: #16a085;"><strong style="color: #27ae60;">【Pre-2 暗唱】</strong> <strong>${g3}</strong></div>
  <div style="font-size: 0.92em; color: #34495e; background-color: #ffffff; padding: 8px 12px; border-left: 4px solid #3498db; border-radius: 4px;">💡 <strong>解説・試験活用</strong>：${nuance}</div>
</div>`);
      }
    } else {
      if (inTable) {
        inTable = false;
      }
      newLines.push(line);
    }
  }

  html = newLines.join('\n');
  const blocks = html.split(/\n\n+/);
  html = blocks.map(b => {
    b = b.trim();
    if (!b) return '';
    if (b.startsWith('<h') || b.startsWith('<div') || b.startsWith('<ul') || b.startsWith('<ol') || b.startsWith('<p') || b.startsWith('<!--') || b.startsWith('<hr')) {
      return b;
    }
    return `<p>${b.replace(/\n/g, '<br>')}</p>`;
  }).join('\n\n');

  return html;
}

let bodyContent = '';
let fullMarkdown = '';

files.forEach((file, index) => {
  const filePath = path.join(kindleDir, file);
  if (fs.existsSync(filePath)) {
    const mdText = fs.readFileSync(filePath, 'utf8');
    fullMarkdown += mdText + '\n\n';
    bodyContent += mdToHtml(mdText);
    if (index < files.length - 1) {
      bodyContent += '\n\n<hr style="margin: 3em 0;" />\n\n';
    }
  }
});

// Write master combined markdown for Vol 2
fs.writeFileSync(path.join(kindleDir, 'eikenPre2_fables_vol2_full.md'), fullMarkdown, 'utf8');

const fullHtml = `<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>英検ステップアップ多読：イソップ寓話編 第2巻（3級 ➔ 準2級対比学習）</title>
  <style>
    body {
      font-family: "Hiragino Mincho ProN", "Yu Mincho", "Georgia", serif;
      line-height: 1.8;
      margin: 0 auto;
      max-width: 800px;
      padding: 20px;
      color: #111;
    }
    h1 {
      font-size: 2em;
      text-align: center;
      margin-top: 2em;
      margin-bottom: 1em;
      color: #1a252c;
    }
    h2 {
      font-size: 1.5em;
      color: #2c3e50;
      border-bottom: 2px solid #3498db;
      padding-bottom: 0.3em;
      margin-top: 2em;
    }
    h3 {
      font-size: 1.2em;
      color: #34495e;
      margin-top: 1.5em;
    }
    p {
      text-indent: 1em;
      margin-bottom: 1em;
    }
    .center {
      text-align: center;
      margin: 20px 0;
    }
    img {
      max-width: 100%;
      height: auto;
    }
    hr {
      border: none;
      border-top: 1px solid #ccc;
      margin: 2.5em 0;
    }
  </style>
</head>
<body>

${bodyContent}

</body>
</html>`;

fs.writeFileSync(path.join(zipBuildDir, 'index.html'), fullHtml, 'utf8');
console.log(`Successfully built Vol 2 package (${files.length} files).`);
