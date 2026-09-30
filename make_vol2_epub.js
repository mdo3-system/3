const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;
const buildDir = path.join(kindleDir, 'vol2_epub_build');
const oebpsDir = path.join(buildDir, 'OEBPS');
const imagesBuildDir = path.join(oebpsDir, 'images');
const metaInfDir = path.join(buildDir, 'META-INF');

try {
  if (fs.existsSync(buildDir)) {
    fs.rmSync(buildDir, { recursive: true, force: true });
  }
} catch (e) {}

fs.mkdirSync(buildDir, { recursive: true });
fs.mkdirSync(oebpsDir, { recursive: true });
fs.mkdirSync(imagesBuildDir, { recursive: true });
fs.mkdirSync(metaInfDir, { recursive: true });

fs.writeFileSync(path.join(buildDir, 'mimetype'), 'application/epub+zip', 'ascii');

const containerXml = `<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>`;
fs.writeFileSync(path.join(metaInfDir, 'container.xml'), containerXml, 'utf8');

const cssContent = `
body { font-family: sans-serif; margin: 5%; line-height: 1.6; color: #111; }
h1 { font-size: 1.8em; text-align: center; color: #1a252c; margin-top: 1em; margin-bottom: 0.5em; }
h2 { font-size: 1.4em; color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 0.3em; margin-top: 1.5em; }
h3 { font-size: 1.1em; color: #34495e; }
p { text-indent: 1em; margin-bottom: 0.8em; }
.center { text-align: center; margin: 1.5em 0; }
ul, ol { padding-left: 1.5em; }
li { margin-bottom: 0.4em; }
.cover-img { max-width: 100%; height: auto; display: block; margin: 0 auto; }
hr { border: none; border-top: 1px solid #ccc; margin: 2em 0; }

.comparison-card {
  border: 1px solid #3498db;
  border-radius: 8px;
  padding: 12px 16px;
  margin: 18px 0;
  background-color: #f8f9fa;
}
.card-header {
  font-weight: bold;
  color: #2c3e50;
  font-size: 1.05em;
  border-bottom: 1px solid #d6dbdf;
  padding-bottom: 6px;
  margin-bottom: 10px;
}
.card-row-g4 { margin-bottom: 8px; color: #444; }
.card-row-g3 { margin-bottom: 10px; color: #16a085; }
.card-badge-g4 { font-weight: bold; color: #7f8c8d; margin-right: 8px; }
.card-badge-g3 { font-weight: bold; color: #27ae60; margin-right: 8px; }
.card-note {
  font-size: 0.92em;
  color: #34495e;
  background-color: #ffffff;
  padding: 8px 12px;
  border-left: 4px solid #3498db;
  border-radius: 4px;
}
`;
fs.writeFileSync(path.join(oebpsDir, 'style.css'), cssContent, 'utf8');

function escapeXml(str) {
  return str.replace(/&(?!amp;|lt;|gt;|quot;|apos;)/g, '&amp;');
}

function mdToXhtml(md) {
  let text = escapeXml(md);
  text = text.replace(/<div style="page-break-before: always;"><\/div>/g, '');
  text = text.replace(/<hr\s*\/?>/g, '<hr />');

  text = text.replace(/^# (.*$)/gim, '<h1>$1</h1>');
  text = text.replace(/^## (.*$)/gim, '<h2>$1</h2>');
  text = text.replace(/^### (.*$)/gim, '<h3>$1</h3>');

  text = text.replace(/<img src="images\/(.*?)" alt="(.*?)" style=".*?" \/>/g, '<div class="center"><img src="images/$1" alt="$2" class="cover-img" /></div>');
  text = text.replace(/!\[(.*?)\]\(images\/(.*?)\)/g, '<div class="center"><img src="images/$2" alt="$1" class="cover-img" /></div>');

  text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
  text = text.replace(/`(.*?)`/g, '<code>$1</code>');

  const lines = text.split('\n');
  let inTable = false;
  let newLines = [];
  let tableHeader = true;

  for (let line of lines) {
    const trimmed = line.trim();
    if (trimmed === '---') {
      if (inTable) inTable = false;
      newLines.push('<hr />');
      continue;
    }
    if (trimmed.startsWith('|')) {
      if (!inTable) {
        inTable = true;
        tableHeader = true;
      }
      if (trimmed.includes('---') || /^\|?[\s:-]+\|?$/.test(trimmed)) continue;
      const cells = line.split('|').filter((_, idx, arr) => idx > 0 && idx < arr.length - 1).map(c => c.trim());
      if (tableHeader) {
        tableHeader = false;
      } else if (cells.length >= 4) {
        const [scene, g4, g3, nuance] = cells;
        newLines.push(`
<div class="comparison-card">
  <div class="card-header">📌 場面：${scene}</div>
  <div class="card-row-g4"><span class="card-badge-g4">【Grade 3 基礎】</span> ${g4}</div>
  <div class="card-row-g3"><span class="card-badge-g3">【Pre-2 暗唱】</span> <strong>${g3}</strong></div>
  <div class="card-note">💡 <strong>解説・試験活用</strong>：${nuance}</div>
</div>`);
      }
    } else {
      if (inTable) {
        inTable = false;
      }
      newLines.push(line);
    }
  }

  text = newLines.join('\n');
  const blocks = text.split(/\n\n+/);
  text = blocks.map(b => {
    b = b.trim();
    if (!b) return '';
    if (b.startsWith('<h') || b.startsWith('<div') || b.startsWith('<ul') || b.startsWith('<ol') || b.startsWith('<p') || b.startsWith('<!--') || b.startsWith('<hr')) {
      return b;
    }
    return `<p>${b.replace(/\n/g, '<br />')}</p>`;
  }).join('\n\n');

  return text;
}

const chapters = [
  { id: 'intro', file: 'vol2_00_introduction.md', title: 'はじめに・構成と学習法' },
  { id: 'ch01', file: 'vol2_chapter01_tortoise_and_hare.md', title: '第1話：ウサギとカメ' },
  { id: 'ch02', file: 'vol2_chapter02_boy_who_cried_wolf.md', title: '第2話：オオカミ少年' },
  { id: 'ch03', file: 'vol2_chapter03_north_wind_and_sun.md', title: '第3話：北風と太陽' },
  { id: 'ch04', file: 'vol2_chapter04_lion_and_mouse.md', title: '第4話：ライオンとネズミ' },
  { id: 'ch05', file: 'vol2_chapter05_ant_and_grasshopper.md', title: '第5話：アリとキリギリス' },
  { id: 'ch06', file: 'vol2_chapter06_fox_and_grapes.md', title: '第6話：キツネとブドウ' },
  { id: 'ch07', file: 'vol2_chapter07_town_mouse_country_mouse.md', title: '第7話：田舎のネズミと街のネズミ' },
  { id: 'ch08', file: 'vol2_chapter08_crow_and_pitcher.md', title: '第8話：カラスと水つぼ' },
  { id: 'ch09', file: 'vol2_chapter09_dog_and_his_shadow.md', title: '第9話：欲張りな犬' },
  { id: 'ch10', file: 'vol2_chapter10_milkmaid_and_her_pail.md', title: '第10話：ミルク搾りの娘' },
  { id: 'epilogue', file: 'vol2_99_epilogue_and_next_volume.md', title: 'おわりに ＆ 次巻のご案内' }
];

const coverHtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <title>Cover</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
  <style type="text/css">
    @page { padding: 0; margin: 0; }
    body { text-align: center; padding: 0; margin: 0; }
    img { max-width: 100%; height: 100%; }
  </style>
</head>
<body>
  <div>
    <img src="images/cover_kdp.jpg" alt="Book Cover"/>
  </div>
</body>
</html>`;
fs.writeFileSync(path.join(oebpsDir, 'cover.xhtml'), coverHtml, 'utf8');

// Extract ONLY images actually used in this volume
const usedImageSet = new Set(['cover_kdp.jpg']);
chapters.forEach(ch => {
  const mdPath = path.join(kindleDir, ch.file);
  if (fs.existsSync(mdPath)) {
    const text = fs.readFileSync(mdPath, 'utf8');
    const matches = text.match(/images\/([^\s\)\"\'>]+)/g) || [];
    matches.forEach(m => usedImageSet.add(m.replace('images/', '')));
  }
});
const srcImagesDir = path.join(kindleDir, 'images');
const images = Array.from(usedImageSet).filter(img => fs.existsSync(path.join(srcImagesDir, img)));

images.forEach(img => {
  fs.copyFileSync(path.join(srcImagesDir, img), path.join(imagesBuildDir, img));
});


chapters.forEach(ch => {
  const mdPath = path.join(kindleDir, ch.file);
  const mdText = fs.readFileSync(mdPath, 'utf8');
  const bodyHtml = mdToXhtml(mdText);

  const xhtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <title>${escapeXml(ch.title)}</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
${bodyHtml}
</body>
</html>`;

  fs.writeFileSync(path.join(oebpsDir, `${ch.id}.xhtml`), xhtml, 'utf8');
});

const navHtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en" lang="en">
<head>
  <title>Table of Contents</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>目次 (Table of Contents)</h1>
    <ol>
      ${chapters.map(c => `<li><a href="${c.id}.xhtml">${escapeXml(c.title)}</a></li>`).join('\n      ')}
    </ol>
  </nav>
</body>
</html>`;
fs.writeFileSync(path.join(oebpsDir, 'nav.xhtml'), navHtml, 'utf8');

const bookUuid = 'urn:uuid:e13e4101-0002-4000-8000-000000000002';

const ncx = `<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="${bookUuid}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>英検ステップアップ多読：イソップ寓話編 第2巻</text>
  </docTitle>
  <navMap>
    ${chapters.map((c, idx) => `
    <navPoint id="navPoint-${idx + 1}" playOrder="${idx + 1}">
      <navLabel><text>${escapeXml(c.title)}</text></navLabel>
      <content src="${c.id}.xhtml"/>
    </navPoint>`).join('')}
  </navMap>
</ncx>`;
fs.writeFileSync(path.join(oebpsDir, 'toc.ncx'), ncx, 'utf8');

const opf = `<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">${bookUuid}</dc:identifier>
    <dc:title>英検ステップアップ多読：イソップ寓話編 第2巻（3級 ➔ 準2級対比学習）</dc:title>
    <dc:language>ja</dc:language>
    <dc:creator>Eiken Fables Publishing Team</dc:creator>
    <meta property="dcterms:modified">2026-09-20T12:00:00Z</meta>
    <meta name="cover" content="cover-image"/>
  </metadata>

  <manifest>
    <item id="style" href="style.css" media-type="text/css"/>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="cover-page" href="cover.xhtml" media-type="application/xhtml+xml"/>
    <item id="cover-image" href="images/cover_kdp.jpg" media-type="image/jpeg" properties="cover-image"/>
    
    ${chapters.map(c => `<item id="${c.id}" href="${c.id}.xhtml" media-type="application/xhtml+xml"/>`).join('\n    ')}
    
    ${images.filter(img => img !== 'cover_kdp.jpg').map(img => {
      const ext = path.extname(img).toLowerCase();
      const mediaType = ext === '.jpg' || ext === '.jpeg' ? 'image/jpeg' : 'image/png';
      return `<item id="img-${img.replace(/[^a-zA-Z0-9]/g, '_')}" href="images/${img}" media-type="${mediaType}"/>`;
    }).join('\n    ')}
  </manifest>

  <spine toc="ncx">
    <itemref idref="cover-page"/>
    <itemref idref="nav"/>
    ${chapters.map(c => `<itemref idref="${c.id}"/>`).join('\n    ')}
  </spine>
</package>`;

fs.writeFileSync(path.join(oebpsDir, 'content.opf'), opf, 'utf8');

console.log('Vol 2 EPUB structure generated.');
