const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;
const srcImagesDir = path.join(kindleDir, 'images');

const allFiles = fs.readdirSync(srcImagesDir);
const validImageExts = ['.png', '.jpg', '.jpeg'];
const validImages = allFiles.filter(f => validImageExts.includes(path.extname(f).toLowerCase()));

const volumes = [
  {
    num: 5,
    prefix: 'vol5',
    title: '英検ステップアップ多読：イソップ寓話編 第5巻（4級 ➔ 3級対比学習・第2集）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第5巻',
    id: 'urn:uuid:e13e4101-0005-4000-8000-000000000005',
    coverImg: 'vol5_cover.jpg',
    koboCoverImg: 'kobo_vol5_cover.jpg',
    fullMdName: 'eiken3_fables_vol5_full.md',
    chapters: [
      { id: 'intro', file: 'vol5_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch11', file: 'chapter11_honest_woodcutter.md', title: '第11話：金の斧と銀の斧' },
      { id: 'ch12', file: 'chapter12_goose_golden_eggs.md', title: '第12話：金の卵を産むガチョウ' },
      { id: 'ch13', file: 'chapter13_wolf_in_sheeps_clothing.md', title: '第13話：羊の皮をかぶった狼' },
      { id: 'ch14', file: 'chapter14_fox_and_stork.md', title: '第14話：キツネとツル' },
      { id: 'ch15', file: 'chapter15_frog_and_ox.md', title: '第15話：カエルと牛' },
      { id: 'ch16', file: 'chapter16_bat_birds_beasts.md', title: '第16話：コウモリと鳥と獣' },
      { id: 'ch17', file: 'chapter17_belling_the_cat.md', title: '第17話：ネズミの会議' },
      { id: 'ch18', file: 'chapter18_bear_and_two_travelers.md', title: '第18話：旅人とクマ' },
      { id: 'ch19', file: 'chapter19_lions_share.md', title: '第19話：獅子の分け前' },
      { id: 'ch20', file: 'chapter20_frog_and_mouse.md', title: '第20話：ネズミとカエル' },
      { id: 'epilogue', file: 'vol5_99_epilogue.md', title: 'おわりに ＆ 次巻のご案内' }
    ]
  },
  {
    num: 6,
    prefix: 'vol6',
    title: '英検ステップアップ多読：イソップ寓話編 第6巻（3級 ➔ 準2級対比学習・第2集）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第6巻',
    id: 'urn:uuid:e13e4101-0006-4000-8000-000000000006',
    coverImg: 'vol6_cover.jpg',
    koboCoverImg: 'kobo_vol6_cover.jpg',
    fullMdName: 'eikenPre2_fables_vol6_full.md',
    chapters: [
      { id: 'intro', file: 'vol6_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch11', file: 'vol2_chapter11_honest_woodcutter.md', title: '第11話：金の斧と銀の斧' },
      { id: 'ch12', file: 'vol2_chapter12_goose_golden_eggs.md', title: '第12話：金の卵を産むガチョウ' },
      { id: 'ch13', file: 'vol2_chapter13_wolf_in_sheeps_clothing.md', title: '第13話：羊の皮をかぶった狼' },
      { id: 'ch14', file: 'vol2_chapter14_fox_and_stork.md', title: '第14話：キツネとツル' },
      { id: 'ch15', file: 'vol2_chapter15_frog_and_ox.md', title: '第15話：カエルと牛' },
      { id: 'ch16', file: 'vol2_chapter16_bat_birds_beasts.md', title: '第16話：コウモリと鳥と獣' },
      { id: 'ch17', file: 'vol2_chapter17_belling_the_cat.md', title: '第17話：ネズミの会議' },
      { id: 'ch18', file: 'vol2_chapter18_bear_and_two_travelers.md', title: '第18話：旅人とクマ' },
      { id: 'ch19', file: 'vol2_chapter19_lions_share.md', title: '第19話：獅子の分け前' },
      { id: 'ch20', file: 'vol2_chapter20_frog_and_mouse.md', title: '第20話：ネズミとカエル' },
      { id: 'epilogue', file: 'vol6_99_epilogue.md', title: 'おわりに ＆ 次巻のご案内' }
    ]
  },
  {
    num: 7,
    prefix: 'vol7',
    title: '英検ステップアップ多読：イソップ寓話編 第7巻（準2級 ➔ 2級対比学習・第2集）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第7巻',
    id: 'urn:uuid:e13e4101-0007-4000-8000-000000000007',
    coverImg: 'vol7_cover.jpg',
    koboCoverImg: 'kobo_vol7_cover.jpg',
    fullMdName: 'eiken2_fables_vol7_full.md',
    chapters: [
      { id: 'intro', file: 'vol7_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch11', file: 'vol3_chapter11_honest_woodcutter.md', title: '第11話：金の斧と銀の斧' },
      { id: 'ch12', file: 'vol3_chapter12_goose_golden_eggs.md', title: '第12話：金の卵を産むガチョウ' },
      { id: 'ch13', file: 'vol3_chapter13_wolf_in_sheeps_clothing.md', title: '第13話：羊の皮をかぶった狼' },
      { id: 'ch14', file: 'vol3_chapter14_fox_and_stork.md', title: '第14話：キツネとツル' },
      { id: 'ch15', file: 'vol3_chapter15_frog_and_ox.md', title: '第15話：カエルと牛' },
      { id: 'ch16', file: 'vol3_chapter16_bat_birds_beasts.md', title: '第16話：コウモリと鳥と獣' },
      { id: 'ch17', file: 'vol3_chapter17_belling_the_cat.md', title: '第17話：ネズミの会議' },
      { id: 'ch18', file: 'vol3_chapter18_bear_and_two_travelers.md', title: '第18話：旅人とクマ' },
      { id: 'ch19', file: 'vol3_chapter19_lions_share.md', title: '第19話：獅子の分け前' },
      { id: 'ch20', file: 'vol3_chapter20_frog_and_mouse.md', title: '第20話：ネズミとカエル' },
      { id: 'epilogue', file: 'vol7_99_epilogue.md', title: 'おわりに ＆ 次巻のご案内' }
    ]
  },
  {
    num: 8,
    prefix: 'vol8',
    title: '英検ステップアップ多読：イソップ寓話編 第8巻（2級 ➔ 準1級対比学習・第2集）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第8巻',
    id: 'urn:uuid:e13e4101-0008-4000-8000-000000000008',
    coverImg: 'vol8_cover.jpg',
    koboCoverImg: 'kobo_vol8_cover.jpg',
    fullMdName: 'eikenPre1_fables_vol8_full.md',
    chapters: [
      { id: 'intro', file: 'vol8_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch11', file: 'vol4_chapter11_honest_woodcutter.md', title: '第11話：金の斧と銀の斧' },
      { id: 'ch12', file: 'vol4_chapter12_goose_golden_eggs.md', title: '第12話：金の卵を産むガチョウ' },
      { id: 'ch13', file: 'vol4_chapter13_wolf_in_sheeps_clothing.md', title: '第13話：羊の皮をかぶった狼' },
      { id: 'ch14', file: 'vol4_chapter14_fox_and_stork.md', title: '第14話：キツネとツル' },
      { id: 'ch15', file: 'vol4_chapter15_frog_and_ox.md', title: '第15話：カエルと牛' },
      { id: 'ch16', file: 'vol4_chapter16_bat_birds_beasts.md', title: '第16話：コウモリと鳥と獣' },
      { id: 'ch17', file: 'vol4_chapter17_belling_the_cat.md', title: '第17話：ネズミの会議' },
      { id: 'ch18', file: 'vol4_chapter18_bear_and_two_travelers.md', title: '第18話：旅人とクマ' },
      { id: 'ch19', file: 'vol4_chapter19_lions_share.md', title: '第19話：獅子の分け前' },
      { id: 'ch20', file: 'vol4_chapter20_frog_and_mouse.md', title: '第20話：ネズミとカエル' },
      { id: 'epilogue', file: 'vol8_99_epilogue.md', title: 'おわりに ＆ 次巻のご案内' }
    ]
  }
];

function escapeXml(str) {
  return str.replace(/&(?!amp;|lt;|gt;|quot;|apos;)/g, '&amp;');
}

const sharedCss = `
body { font-family: "Hiragino Mincho ProN", "Yu Mincho", "Georgia", serif; margin: 5%; line-height: 1.7; color: #111; }
h1 { font-size: 1.8em; text-align: center; color: #1a252c; margin-top: 1em; margin-bottom: 0.5em; }
h2 { font-size: 1.35em; color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 0.3em; margin-top: 1.5em; }
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
.card-row-g4, .card-row-g3-base, .card-row-pre2-base, .card-row-g2-base { margin-bottom: 8px; color: #444; }
.card-row-g3, .card-row-pre2, .card-row-g2, .card-row-pre1 { margin-bottom: 10px; color: #16a085; }
.card-badge-g4, .card-badge-g3-base, .card-badge-pre2-base, .card-badge-g2-base { font-weight: bold; color: #7f8c8d; margin-right: 8px; }
.card-badge-g3, .card-badge-pre2, .card-badge-g2, .card-badge-pre1 { font-weight: bold; color: #27ae60; margin-right: 8px; }
.card-note {
  font-size: 0.92em;
  color: #34495e;
  background-color: #ffffff;
  padding: 8px 12px;
  border-left: 4px solid #3498db;
  border-radius: 4px;
}
blockquote {
  border-left: 4px solid #f39c12;
  margin: 1.5em 0;
  padding: 0.8em 1.2em;
  background-color: #fcf8e3;
  color: #8a6d3b;
}
`;

function mdToXhtml(md) {
  let text = escapeXml(md);
  text = text.replace(/<div style="page-break-before: always;"><\/div>/g, '');
  text = text.replace(/<hr\s*\/?>/g, '<hr />');
  text = text.replace(/---/g, '<hr />');

  text = text.replace(/^# (.*$)/gim, '<h1>$1</h1>');
  text = text.replace(/^## (.*$)/gim, '<h2>$1</h2>');
  text = text.replace(/^### (.*$)/gim, '<h3>$1</h3>');

  text = text.replace(/<img src="images\/(.*?)" alt="(.*?)" style=".*?" \/>/g, '<div class="center"><img src="images/$1" alt="$2" class="cover-img" /></div>');
  text = text.replace(/!\[(.*?)\]\(images\/(.*?)\)/g, '<div class="center"><img src="images/$2" alt="$1" class="cover-img" /></div>');

  text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
  text = text.replace(/`(.*?)`/g, '<code>$1</code>');

  const blocks = text.split(/\n\n+/);
  text = blocks.map(b => {
    b = b.trim();
    if (!b) return '';
    if (b.startsWith('<h') || b.startsWith('<div') || b.startsWith('<ul') || b.startsWith('<ol') || b.startsWith('<p') || b.startsWith('<!--') || b.startsWith('<hr') || b.startsWith('<blockquote') || b.startsWith('<pre')) {
      return b;
    }
    return `<p>${b.replace(/\n/g, '<br />')}</p>`;
  }).join('\n\n');

  return text;
}

volumes.forEach(vol => {
  console.log(`\n========================================`);
  console.log(`BUILDING PHASE 2 VOLUME ${vol.num} (${vol.prefix})`);
  console.log(`========================================`);

  // 1. KDP ZIP Directory
  const kdpZipDir = path.join(kindleDir, `${vol.prefix}_kdp_zip_build`);
  const kdpImagesDir = path.join(kdpZipDir, 'images');
  if (fs.existsSync(kdpZipDir)) {
    fs.rmSync(kdpZipDir, { recursive: true, force: true });
  }
  fs.mkdirSync(kdpZipDir, { recursive: true });
  fs.mkdirSync(kdpImagesDir, { recursive: true });

  // 2. EPUB Directory
  const epubBuildDir = path.join(kindleDir, `${vol.prefix}_epub_build`);
  const oebpsDir = path.join(epubBuildDir, 'OEBPS');
  const epubImagesDir = path.join(oebpsDir, 'images');
  const metaInfDir = path.join(epubBuildDir, 'META-INF');
  if (fs.existsSync(epubBuildDir)) {
    fs.rmSync(epubBuildDir, { recursive: true, force: true });
  }
  fs.mkdirSync(epubBuildDir, { recursive: true });
  fs.mkdirSync(oebpsDir, { recursive: true });
  fs.mkdirSync(epubImagesDir, { recursive: true });
  fs.mkdirSync(metaInfDir, { recursive: true });

  // Extract ONLY images actually used in this volume
  const volUsedImageSet = new Set([vol.coverImg]);
  vol.chapters.forEach(ch => {
    const mdPath = path.join(kindleDir, ch.file);
    if (fs.existsSync(mdPath)) {
      const text = fs.readFileSync(mdPath, 'utf8');
      const matches = text.match(/images\/([^\s\)\"\'>]+)/g) || [];
      matches.forEach(m => volUsedImageSet.add(m.replace('images/', '')));
    }
  });
  const volImages = Array.from(volUsedImageSet).filter(img => fs.existsSync(path.join(srcImagesDir, img)));

  // Copy images
  volImages.forEach(img => {
    fs.copyFileSync(path.join(srcImagesDir, img), path.join(kdpImagesDir, img));
    fs.copyFileSync(path.join(srcImagesDir, img), path.join(epubImagesDir, img));
  });


  // Write mimetype & container.xml
  fs.writeFileSync(path.join(epubBuildDir, 'mimetype'), 'application/epub+zip', 'ascii');
  const containerXml = `<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>`;
  fs.writeFileSync(path.join(metaInfDir, 'container.xml'), containerXml, 'utf8');

  // Stylesheet
  fs.writeFileSync(path.join(oebpsDir, 'style.css'), sharedCss, 'utf8');

  // Cover Page
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
    <img src="images/${vol.coverImg}" alt="Book Cover"/>
  </div>
</body>
</html>`;
  fs.writeFileSync(path.join(oebpsDir, 'cover.xhtml'), coverHtml, 'utf8');

  // Compile full markdown and individual XHTML chapters
  let fullMarkdown = '';
  let kdpBodyHtml = '';

  vol.chapters.forEach((ch, idx) => {
    const mdPath = path.join(kindleDir, ch.file);
    if (!fs.existsSync(mdPath)) {
      console.error(`ERROR: Missing file: ${mdPath}`);
      return;
    }
    const mdContent = fs.readFileSync(mdPath, 'utf8');
    fullMarkdown += mdContent + '\n\n';

    const chapterHtml = mdToXhtml(mdContent);
    kdpBodyHtml += chapterHtml;
    if (idx < vol.chapters.length - 1) {
      kdpBodyHtml += '\n\n<hr style="margin: 3em 0;" />\n\n';
    }

    const chapterXhtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <title>${escapeXml(ch.title)}</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
${chapterHtml}
</body>
</html>`;
    fs.writeFileSync(path.join(oebpsDir, `${ch.id}.xhtml`), chapterXhtml, 'utf8');
  });

  // Save Master Combined Markdown
  fs.writeFileSync(path.join(kindleDir, vol.fullMdName), fullMarkdown, 'utf8');
  console.log(`Saved Full Combined Markdown -> ${vol.fullMdName}`);

  // Save KDP index.html
  const kdpIndexHtml = `<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>${escapeXml(vol.title)}</title>
  <style>
${sharedCss}
  </style>
</head>
<body>
  <div style="text-align: center; margin-bottom: 40px;">
    <img src="images/${vol.coverImg}" alt="Cover" style="max-width: 90%; height: auto;" />
  </div>
${kdpBodyHtml}
</body>
</html>`;
  fs.writeFileSync(path.join(kdpZipDir, 'index.html'), kdpIndexHtml, 'utf8');
  console.log(`Saved KDP HTML -> ${vol.prefix}_kdp_zip_build/index.html`);

  // Nav XHTML
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
      ${vol.chapters.map(c => `<li><a href="${c.id}.xhtml">${escapeXml(c.title)}</a></li>`).join('\n      ')}
    </ol>
  </nav>
</body>
</html>`;
  fs.writeFileSync(path.join(oebpsDir, 'nav.xhtml'), navHtml, 'utf8');

  // NCX
  const ncx = `<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="${vol.id}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>${escapeXml(vol.shortTitle)}</text>
  </docTitle>
  <navMap>
    ${vol.chapters.map((c, idx) => `
    <navPoint id="navPoint-${idx + 1}" playOrder="${idx + 1}">
      <navLabel><text>${escapeXml(c.title)}</text></navLabel>
      <content src="${c.id}.xhtml"/>
    </navPoint>`).join('')}
  </navMap>
</ncx>`;
  fs.writeFileSync(path.join(oebpsDir, 'toc.ncx'), ncx, 'utf8');

  // OPF
  const opf = `<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">${vol.id}</dc:identifier>
    <dc:title>${escapeXml(vol.title)}</dc:title>
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
    <item id="cover-image" href="images/${vol.coverImg}" media-type="image/jpeg" properties="cover-image"/>
    
    ${vol.chapters.map(c => `<item id="${c.id}" href="${c.id}.xhtml" media-type="application/xhtml+xml"/>`).join('\n    ')}
    
    ${volImages.filter(img => img !== vol.coverImg).map(img => {
      const ext = path.extname(img).toLowerCase();
      const mediaType = ext === '.jpg' || ext === '.jpeg' ? 'image/jpeg' : 'image/png';
      return `<item id="img-${img.replace(/[^a-zA-Z0-9]/g, '_')}" href="images/${img}" media-type="${mediaType}"/>`;
    }).join('\n    ')}
  </manifest>

  <spine toc="ncx">
    <itemref idref="cover-page"/>
    <itemref idref="nav"/>
    ${vol.chapters.map(c => `<itemref idref="${c.id}"/>`).join('\n    ')}
  </spine>
</package>`;
  fs.writeFileSync(path.join(oebpsDir, 'content.opf'), opf, 'utf8');

  console.log(`Generated EPUB3 structure -> ${vol.prefix}_epub_build`);
});

console.log('\nSUCCESS: All Volume 5, 6, 7, 8 build directories created!');
