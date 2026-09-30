const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;
const buildDir = path.join(kindleDir, 'epub_build');
const oebpsDir = path.join(buildDir, 'OEBPS');
const imagesBuildDir = path.join(oebpsDir, 'images');
const metaInfDir = path.join(buildDir, 'META-INF');

// Clean build folder
try {
  if (fs.existsSync(buildDir)) {
    fs.rmSync(buildDir, { recursive: true, force: true });
  }
} catch (e) {
  console.log('Build dir clean skipped:', e.message);
}

fs.mkdirSync(buildDir, { recursive: true });
fs.mkdirSync(oebpsDir, { recursive: true });
fs.mkdirSync(imagesBuildDir, { recursive: true });
fs.mkdirSync(metaInfDir, { recursive: true });

// 1. Create mimetype
fs.writeFileSync(path.join(buildDir, 'mimetype'), 'application/epub+zip', 'utf8');

// 2. Create META-INF/container.xml
const containerXml = `<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>`;
fs.writeFileSync(path.join(metaInfDir, 'container.xml'), containerXml, 'utf8');

// 3. Create OEBPS/style.css
const cssContent = `
body { font-family: serif; margin: 5%; line-height: 1.6; }
h1 { font-size: 1.8em; text-align: center; color: #1a252c; margin-top: 1em; margin-bottom: 0.5em; }
h2 { font-size: 1.4em; color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 0.3em; margin-top: 1.5em; }
h3 { font-size: 1.1em; color: #34495e; }
p { text-indent: 1em; margin-bottom: 0.8em; }
p.no-indent { text-indent: 0; }
.page-break { page-break-before: always; clear: both; }
.center { text-align: center; }
table { width: 100%; border-collapse: collapse; margin: 1.5em 0; }
th, td { border: 1px solid #bdc3c7; padding: 8px 12px; text-align: left; font-size: 0.9em; }
th { background-color: #ecf0f1; }
ul, ol { padding-left: 1.5em; }
li { margin-bottom: 0.4em; }
.cover-img { max-width: 100%; height: auto; display: block; margin: 0 auto; }
`;
fs.writeFileSync(path.join(oebpsDir, 'style.css'), cssContent, 'utf8');

function mdToHtml(md) {
  let html = md;
  html = html.replace(/<div style="page-break-before: always;"><\/div>/g, '<div class="page-break"></div>');
  html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');
  html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
  html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
  html = html.replace(/<img src="images\/(.*?)" alt="(.*?)" style=".*?" \/>/g, '<div class="center"><img src="images/$1" alt="$2" class="cover-img" /></div>');
  html = html.replace(/!\[(.*?)\]\(images\/(.*?)\)/g, '<div class="center"><img src="images/$2" alt="$1" class="cover-img" /></div>');
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');

  const lines = html.split('\n');
  let inTable = false;
  let newLines = [];
  let tableHeader = true;

  for (let line of lines) {
    if (line.trim().startsWith('|')) {
      if (!inTable) {
        inTable = true;
        tableHeader = true;
        newLines.push('<table>');
      }
      if (line.includes('---')) continue;
      const cells = line.split('|').filter((_, idx, arr) => idx > 0 && idx < arr.length - 1).map(c => c.trim());
      if (tableHeader) {
        newLines.push('  <thead><tr>' + cells.map(c => `<th>${c}</th>`).join('') + '</tr></thead><tbody>');
        tableHeader = false;
      } else {
        newLines.push('  <tr>' + cells.map(c => `<td>${c}</td>`).join('') + '</tr>');
      }
    } else {
      if (inTable) {
        inTable = false;
        newLines.push('  </tbody></table>');
      }
      newLines.push(line);
    }
  }
  if (inTable) newLines.push('  </tbody></table>');

  html = newLines.join('\n');
  const blocks = html.split(/\n\n+/);
  html = blocks.map(b => {
    b = b.trim();
    if (b.startsWith('<h') || b.startsWith('<table') || b.startsWith('<div') || b.startsWith('<ul') || b.startsWith('<ol') || b.startsWith('<p') || b.startsWith('<!--')) {
      return b;
    }
    return `<p>${b.replace(/\n/g, '<br/>')}</p>`;
  }).join('\n\n');

  return html;
}

const chapters = [
  { id: 'intro', file: '00_introduction.md', title: 'はじめに・構成と学習法' },
  { id: 'ch01', file: 'chapter01_tortoise_and_hare.md', title: '第1話：ウサギとカメ' },
  { id: 'ch02', file: 'chapter02_boy_who_cried_wolf.md', title: '第2話：オオカミ少年' },
  { id: 'ch03', file: 'chapter03_north_wind_and_sun.md', title: '第3話：北風と太陽' },
  { id: 'ch04', file: 'chapter04_lion_and_mouse.md', title: '第4話：ライオンとネズミ' },
  { id: 'ch05', file: 'chapter05_ant_and_grasshopper.md', title: '第5話：アリとキリギリス' },
  { id: 'ch06', file: 'chapter06_fox_and_grapes.md', title: '第6話：キツネとブドウ' },
  { id: 'ch07', file: 'chapter07_town_mouse_country_mouse.md', title: '第7話：田舎のネズミと街のネズミ' },
  { id: 'ch08', file: 'chapter08_crow_and_pitcher.md', title: '第8話：カラスと水つぼ' },
  { id: 'ch09', file: 'chapter09_dog_and_his_shadow.md', title: '第9話：欲張りな犬' },
  { id: 'ch10', file: 'chapter10_milkmaid_and_her_pail.md', title: '第10話：ミルク搾りの娘' },
  { id: 'epilogue', file: '99_epilogue_and_next_volume.md', title: 'おわりに ＆ 次巻のご案内' }
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
    <img src="images/cover.png" alt="Book Cover"/>
  </div>
</body>
</html>`;
fs.writeFileSync(path.join(oebpsDir, 'cover.xhtml'), coverHtml, 'utf8');

const srcImagesDir = path.join(kindleDir, 'images');
const images = fs.readdirSync(srcImagesDir);
images.forEach(img => {
  fs.copyFileSync(path.join(srcImagesDir, img), path.join(imagesBuildDir, img));
});

chapters.forEach(ch => {
  const mdPath = path.join(kindleDir, ch.file);
  const mdText = fs.readFileSync(mdPath, 'utf8');
  const bodyHtml = mdToHtml(mdText);

  const xhtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <title>${ch.title}</title>
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
      ${chapters.map(c => `<li><a href="${c.id}.xhtml">${c.title}</a></li>`).join('\n      ')}
    </ol>
  </nav>
</body>
</html>`;
fs.writeFileSync(path.join(oebpsDir, 'nav.xhtml'), navHtml, 'utf8');

const ncx = `<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:eiken3-fables-vol1-2026"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>英検ステップアップ多読：イソップ寓話編 第1巻</text>
  </docTitle>
  <navMap>
    ${chapters.map((c, idx) => `
    <navPoint id="navPoint-${idx + 1}" playOrder="${idx + 1}">
      <navLabel><text>${c.title}</text></navLabel>
      <content src="${c.id}.xhtml"/>
    </navPoint>`).join('')}
  </navMap>
</ncx>`;
fs.writeFileSync(path.join(oebpsDir, 'toc.ncx'), ncx, 'utf8');

const opf = `<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">urn:uuid:eiken3-fables-vol1-2026</dc:identifier>
    <dc:title>英検ステップアップ多読：イソップ寓話編 第1巻（4級 ➔ 3級対比学習）</dc:title>
    <dc:language>en</dc:language>
    <dc:creator>Eiken Fables Publishing Team</dc:creator>
    <meta property="dcterms:modified">2026-09-20T12:00:00Z</meta>
    <meta name="cover" content="cover-image"/>
  </metadata>

  <manifest>
    <item id="style" href="style.css" media-type="text/css"/>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="cover-page" href="cover.xhtml" media-type="application/xhtml+xml"/>
    <item id="cover-image" href="images/cover.png" media-type="image/png" properties="cover-image"/>
    
    ${chapters.map(c => `<item id="${c.id}" href="${c.id}.xhtml" media-type="application/xhtml+xml"/>`).join('\n    ')}
    
    ${images.map(img => `<item id="img-${img.replace(/[^a-zA-Z0-9]/g, '_')}" href="images/${img}" media-type="image/png"/>`).join('\n    ')}
  </manifest>

  <spine toc="ncx">
    <itemref idref="cover-page"/>
    <itemref idref="nav"/>
    ${chapters.map(c => `<itemref idref="${c.id}"/>`).join('\n    ')}
  </spine>
</package>`;

fs.writeFileSync(path.join(oebpsDir, 'content.opf'), opf, 'utf8');

console.log('Successfully regenerated EPUB structure.');
