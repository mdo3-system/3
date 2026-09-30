const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;
const srcImagesDir = path.join(kindleDir, 'images');

const allFiles = fs.readdirSync(srcImagesDir);
const validImageExts = ['.png', '.jpg', '.jpeg'];
const validImages = allFiles.filter(f => validImageExts.includes(path.extname(f).toLowerCase()));

const volumes = [
  {
    num: 21,
    prefix: 'vol21',
    title: '英検ステップアップ多読：イソップ寓話編 第21巻（4級 ➔ 3級対比学習・第6集 完結編）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第21巻',
    id: 'urn:uuid:e13e4101-0021-4000-8000-000000000021',
    coverImg: 'vol21_cover.jpg',
    koboCoverImg: 'kobo_vol21_cover.jpg',
    fullMdName: 'eiken3_fables_vol21_full.md',
    chapters: [
      { id: 'intro', file: 'vol21_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch51', file: 'chapter51_eagle_and_arrow.md', title: '第51話：鷲と矢' },
      { id: 'ch52', file: 'chapter52_monkey_as_judge.md', title: '第52話：猿の裁判長' },
      { id: 'ch53', file: 'chapter53_miller_son_and_donkey.md', title: '第53話：ロバを売る親子' },
      { id: 'ch54', file: 'chapter54_bee_and_zeus.md', title: '第54話：蜜蜂とゼウス' },
      { id: 'ch55', file: 'chapter55_pig_sheep_and_goat.md', title: '第55話：豚と羊と山羊' },
      { id: 'ch56', file: 'chapter56_sick_raven.md', title: '第56話：病気のカラスと母' },
      { id: 'ch57', file: 'chapter57_spider_and_swallow.md', title: '第57話：クモとツバメ' },
      { id: 'ch58', file: 'chapter58_fisherman_piping.md', title: '第58話：笛を吹く漁師' },
      { id: 'ch59', file: 'chapter59_bear_and_bees.md', title: '第59話：蜂と熊' },
      { id: 'ch60', file: 'chapter60_traveler_and_fortune.md', title: '第60話：旅人と運命の女神' },
      { id: 'epilogue', file: 'vol21_99_epilogue.md', title: 'おわりに ＆ 全60話完結記念' }
    ]
  },
  {
    num: 22,
    prefix: 'vol22',
    title: '英検ステップアップ多読：イソップ寓話編 第22巻（3級 ➔ 準2級対比学習・第6集 完結編）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第22巻',
    id: 'urn:uuid:e13e4101-0022-4000-8000-000000000022',
    coverImg: 'vol22_cover.jpg',
    koboCoverImg: 'kobo_vol22_cover.jpg',
    fullMdName: 'eikenPre2_fables_vol22_full.md',
    chapters: [
      { id: 'intro', file: 'vol22_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch51', file: 'vol2_chapter51_eagle_and_arrow.md', title: '第51話：鷲と矢' },
      { id: 'ch52', file: 'vol2_chapter52_monkey_as_judge.md', title: '第52話：猿の裁判長' },
      { id: 'ch53', file: 'vol2_chapter53_miller_son_and_donkey.md', title: '第53話：ロバを売る親子' },
      { id: 'ch54', file: 'vol2_chapter54_bee_and_zeus.md', title: '第54話：蜜蜂とゼウス' },
      { id: 'ch55', file: 'vol2_chapter55_pig_sheep_and_goat.md', title: '第55話：豚と羊と山羊' },
      { id: 'ch56', file: 'vol2_chapter56_sick_raven.md', title: '第56話：病気のカラスと母' },
      { id: 'ch57', file: 'vol2_chapter57_spider_and_swallow.md', title: '第57話：クモとツバメ' },
      { id: 'ch58', file: 'vol2_chapter58_fisherman_piping.md', title: '第58話：笛を吹く漁師' },
      { id: 'ch59', file: 'vol2_chapter59_bear_and_bees.md', title: '第59話：蜂と熊' },
      { id: 'ch60', file: 'vol2_chapter60_traveler_and_fortune.md', title: '第60話：旅人と運命の女神' },
      { id: 'epilogue', file: 'vol22_99_epilogue.md', title: 'おわりに ＆ 全60話完結記念' }
    ]
  },
  {
    num: 23,
    prefix: 'vol23',
    title: '英検ステップアップ多読：イソップ寓話編 第23巻（準2級 ➔ 2級対比学習・第6集 完結編）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第23巻',
    id: 'urn:uuid:e13e4101-0023-4000-8000-000000000023',
    coverImg: 'vol23_cover.jpg',
    koboCoverImg: 'kobo_vol23_cover.jpg',
    fullMdName: 'eiken2_fables_vol23_full.md',
    chapters: [
      { id: 'intro', file: 'vol23_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch51', file: 'vol3_chapter51_eagle_and_arrow.md', title: '第51話：鷲と矢' },
      { id: 'ch52', file: 'vol3_chapter52_monkey_as_judge.md', title: '第52話：猿の裁判長' },
      { id: 'ch53', file: 'vol3_chapter53_miller_son_and_donkey.md', title: '第53話：ロバを売る親子' },
      { id: 'ch54', file: 'vol3_chapter54_bee_and_zeus.md', title: '第54話：蜜蜂とゼウス' },
      { id: 'ch55', file: 'vol3_chapter55_pig_sheep_and_goat.md', title: '第55話：豚と羊と山羊' },
      { id: 'ch56', file: 'vol3_chapter56_sick_raven.md', title: '第56話：病気のカラスと母' },
      { id: 'ch57', file: 'vol3_chapter57_spider_and_swallow.md', title: '第57話：クモとツバメ' },
      { id: 'ch58', file: 'vol3_chapter58_fisherman_piping.md', title: '第58話：笛を吹く漁師' },
      { id: 'ch59', file: 'vol3_chapter59_bear_and_bees.md', title: '第59話：蜂と熊' },
      { id: 'ch60', file: 'vol3_chapter60_traveler_and_fortune.md', title: '第60話：旅人と運命の女神' },
      { id: 'epilogue', file: 'vol23_99_epilogue.md', title: 'おわりに ＆ 全60話完結記念' }
    ]
  },
  {
    num: 24,
    prefix: 'vol24',
    title: '英検ステップアップ多読：イソップ寓話編 第24巻（2級 ➔ 準1級対比学習・第6集 完結編）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第24巻',
    id: 'urn:uuid:e13e4101-0024-4000-8000-000000000024',
    coverImg: 'vol24_cover.jpg',
    koboCoverImg: 'kobo_vol24_cover.jpg',
    fullMdName: 'eikenPre1_fables_vol24_full.md',
    chapters: [
      { id: 'intro', file: 'vol24_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch51', file: 'vol4_chapter51_eagle_and_arrow.md', title: '第51話：鷲と矢' },
      { id: 'ch52', file: 'vol4_chapter52_monkey_as_judge.md', title: '第52話：猿の裁判長' },
      { id: 'ch53', file: 'vol4_chapter53_miller_son_and_donkey.md', title: '第53話：ロバを売る親子' },
      { id: 'ch54', file: 'vol4_chapter54_bee_and_zeus.md', title: '第54話：蜜蜂とゼウス' },
      { id: 'ch55', file: 'vol4_chapter55_pig_sheep_and_goat.md', title: '第55話：豚と羊と山羊' },
      { id: 'ch56', file: 'vol4_chapter56_sick_raven.md', title: '第56話：病気のカラスと母' },
      { id: 'ch57', file: 'vol4_chapter57_spider_and_swallow.md', title: '第57話：クモとツバメ' },
      { id: 'ch58', file: 'vol4_chapter58_fisherman_piping.md', title: '第58話：笛を吹く漁師' },
      { id: 'ch59', file: 'vol4_chapter59_bear_and_bees.md', title: '第59話：蜂と熊' },
      { id: 'ch60', file: 'vol4_chapter60_traveler_and_fortune.md', title: '第60話：旅人と運命の女神' },
      { id: 'epilogue', file: 'vol24_99_epilogue.md', title: 'おわりに ＆ 全60話完結記念' }
    ]
  }
];

function escapeXml(unsafe) {
  return unsafe
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

const sharedCss = `
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Sans", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
  line-height: 1.7;
  color: #1a1a1a;
  padding: 0 10px;
}
h1 {
  font-size: 1.6em;
  color: #0d1b2a;
  border-bottom: 2px solid #27ae60;
  padding-bottom: 0.3em;
  margin-top: 1.2em;
}
h2 {
  font-size: 1.3em;
  color: #1b4965;
  border-left: 5px solid #27ae60;
  padding-left: 8px;
  margin-top: 1.5em;
}
h3 {
  font-size: 1.1em;
  color: #2c3e50;
  margin-top: 1.2em;
}
p {
  margin: 0.8em 0;
  text-align: justify;
}
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

  text = text.replace(/&lt;div style=&quot;text-align: center; margin-bottom: 20px;&quot;&gt;\s*&lt;img src=&quot;images\/(.*?)&quot; alt=&quot;(.*?)&quot; style=&quot;max-width: 100%; height: auto;&quot; \/&gt;\s*&lt;\/div&gt;/g, '<div class="center"><img src="images/$1" alt="$2" class="cover-img" /></div>');

  text = text.replace(/&lt;div class=&quot;comparison-card&quot;&gt;/g, '<div class="comparison-card">');
  text = text.replace(/&lt;\/div&gt;/g, '</div>');
  text = text.replace(/&lt;div class=&quot;(card-[a-z0-9-]+)&quot;&gt;/g, '<div class="$1">');
  text = text.replace(/&lt;span class=&quot;(card-[a-z0-9-]+)&quot;&gt;(.*?)&lt;\/span&gt;/g, '<span class="$1">$2</span>');
  text = text.replace(/&lt;strong&gt;(.*?)&lt;\/strong&gt;/g, '<strong>$1</strong>');

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
  console.log(`BUILDING PHASE 6 VOLUME ${vol.num} (${vol.prefix})`);
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
  try {
    if (fs.existsSync(epubBuildDir)) {
      fs.rmSync(epubBuildDir, { recursive: true, force: true });
    }
  } catch (e) {}
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
<div style="text-align: center; margin-bottom: 2em;">
  <img src="images/${vol.coverImg}" alt="Cover" style="max-width: 100%; height: auto;" />
</div>
${kdpBodyHtml}
</body>
</html>`;
  fs.writeFileSync(path.join(kdpZipDir, 'index.html'), kdpIndexHtml, 'utf8');

  // OPF Manifest & Spine
  let manifestItems = [
    `<item id="style" href="style.css" media-type="text/css"/>`,
    `<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>`,
    `<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>`,
    `<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>`
  ];

  volImages.forEach((img, i) => {
    const ext = path.extname(img).toLowerCase();
    const mime = ext === '.png' ? 'image/png' : 'image/jpeg';
    let prop = img === vol.coverImg ? ' properties="cover-image"' : '';
    manifestItems.push(`<item id="img_${i}" href="images/${img}" media-type="${mime}"${prop}/>`);
  });

  let spineItems = [
    `<itemref idref="cover" linear="no"/>`
  ];

  vol.chapters.forEach(ch => {
    manifestItems.push(`<item id="${ch.id}" href="${ch.id}.xhtml" media-type="application/xhtml+xml"/>`);
    spineItems.push(`<itemref idref="${ch.id}"/>`);
  });

  const contentOpf = `<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookID" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:title>${escapeXml(vol.title)}</dc:title>
    <dc:creator>英語多読・英検対策研究会</dc:creator>
    <dc:language>ja</dc:language>
    <dc:identifier id="BookID">${vol.id}</dc:identifier>
    <dc:publisher>Antigravity Publishing</dc:publisher>
    <meta property="dcterms:modified">${new Date().toISOString().replace(/\.\d+Z$/, 'Z')}</meta>
    <meta name="cover" content="img_${volImages.indexOf(vol.coverImg)}"/>
  </metadata>
  <manifest>
    ${manifestItems.join('\n    ')}
  </manifest>
  <spine toc="ncx">
    ${spineItems.join('\n    ')}
  </spine>
  <guide>
    <reference type="cover" title="Cover" href="cover.xhtml"/>
    <reference type="toc" title="Table of Contents" href="nav.xhtml"/>
    <reference type="text" title="Beginning" href="intro.xhtml"/>
  </guide>
</package>`;
  fs.writeFileSync(path.join(oebpsDir, 'content.opf'), contentOpf, 'utf8');

  // nav.xhtml
  let navList = vol.chapters.map(ch => `      <li><a href="${ch.id}.xhtml">${escapeXml(ch.title)}</a></li>`).join('\n');
  const navHtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="ja" lang="ja">
<head>
  <title>Table of Contents</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>目次</h1>
    <ol>
${navList}
    </ol>
  </nav>
</body>
</html>`;
  fs.writeFileSync(path.join(oebpsDir, 'nav.xhtml'), navHtml, 'utf8');

  // toc.ncx
  let ncxNavPoints = vol.chapters.map((ch, idx) => `
    <navPoint id="navPoint-${idx + 1}" playOrder="${idx + 1}">
      <navLabel><text>${escapeXml(ch.title)}</text></navLabel>
      <content src="${ch.id}.xhtml"/>
    </navPoint>`).join('');

  const tocNcx = `<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="${vol.id}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>${escapeXml(vol.title)}</text></docTitle>
  <navMap>
${ncxNavPoints}
  </navMap>
</ncx>`;
  fs.writeFileSync(path.join(oebpsDir, 'toc.ncx'), tocNcx, 'utf8');

  console.log(`Generated EPUB and KDP build files for Volume ${vol.num}!`);
});

console.log(`\n========================================`);
console.log(`ALL PHASE 6 VOLUMES (21, 22, 23, 24) BUILT SUCCESSFULLY!`);
console.log(`========================================\n`);
