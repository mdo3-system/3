const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;
const srcImagesDir = path.join(kindleDir, 'images');

const allFiles = fs.readdirSync(srcImagesDir);
const validImageExts = ['.png', '.jpg', '.jpeg'];
const validImages = allFiles.filter(f => validImageExts.includes(path.extname(f).toLowerCase()));

const volumes = [
  {
    num: 17,
    prefix: 'vol17',
    title: '英検ステップアップ多読：イソップ寓話編 第17巻（4級 ➔ 3級対比学習・第5集）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第17巻',
    id: 'urn:uuid:e13e4101-0017-4000-8000-000000000017',
    coverImg: 'vol17_cover.jpg',
    koboCoverImg: 'kobo_vol17_cover.jpg',
    fullMdName: 'eiken3_fables_vol17_full.md',
    chapters: [
      { id: 'intro', file: 'vol17_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch41', file: 'chapter41_old_hound.md', title: '第41話：猟犬と年老いた犬' },
      { id: 'ch42', file: 'chapter42_wall_and_nail.md', title: '第42話：壁と釘' },
      { id: 'ch43', file: 'chapter43_fox_and_hedgehog.md', title: '第43話：虻とキツネ' },
      { id: 'ch44', file: 'chapter44_wild_boar_and_fox.md', title: '第44話：イノシシとキツネ' },
      { id: 'ch45', file: 'chapter45_astronomer.md', title: '第45話：天文学者' },
      { id: 'ch46', file: 'chapter46_thief_and_dog.md', title: '第46話：泥棒と見張り番の犬' },
      { id: 'ch47', file: 'chapter47_lion_and_dolphin.md', title: '第47話：獅子とイルカ' },
      { id: 'ch48', file: 'chapter48_dog_and_wolf.md', title: '第48話：狼と痩せた犬' },
      { id: 'ch49', file: 'chapter49_thief_and_his_mother.md', title: '第49話：盗賊と母' },
      { id: 'ch50', file: 'chapter50_blind_man_and_whelp.md', title: '第50話：盲人と子狼' },
      { id: 'epilogue', file: 'vol17_99_epilogue.md', title: 'おわりに ＆ 次巻のご案内' }
    ]
  },
  {
    num: 18,
    prefix: 'vol18',
    title: '英検ステップアップ多読：イソップ寓話編 第18巻（3級 ➔ 準2級対比学習・第5集）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第18巻',
    id: 'urn:uuid:e13e4101-0018-4000-8000-000000000018',
    coverImg: 'vol18_cover.jpg',
    koboCoverImg: 'kobo_vol18_cover.jpg',
    fullMdName: 'eikenPre2_fables_vol18_full.md',
    chapters: [
      { id: 'intro', file: 'vol18_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch41', file: 'vol2_chapter41_old_hound.md', title: '第41話：猟犬と年老いた犬' },
      { id: 'ch42', file: 'vol2_chapter42_wall_and_nail.md', title: '第42話：壁と釘' },
      { id: 'ch43', file: 'vol2_chapter43_fox_and_hedgehog.md', title: '第43話：虻とキツネ' },
      { id: 'ch44', file: 'vol2_chapter44_wild_boar_and_fox.md', title: '第44話：イノシシとキツネ' },
      { id: 'ch45', file: 'vol2_chapter45_astronomer.md', title: '第45話：天文学者' },
      { id: 'ch46', file: 'vol2_chapter46_thief_and_dog.md', title: '第46話：泥棒と見張り番の犬' },
      { id: 'ch47', file: 'vol2_chapter47_lion_and_dolphin.md', title: '第47話：獅子とイルカ' },
      { id: 'ch48', file: 'vol2_chapter48_dog_and_wolf.md', title: '第48話：狼と痩せた犬' },
      { id: 'ch49', file: 'vol2_chapter49_thief_and_his_mother.md', title: '第49話：盗賊と母' },
      { id: 'ch50', file: 'vol2_chapter50_blind_man_and_whelp.md', title: '第50話：盲人と子狼' },
      { id: 'epilogue', file: 'vol18_99_epilogue.md', title: 'おわりに ＆ 次巻のご案内' }
    ]
  },
  {
    num: 19,
    prefix: 'vol19',
    title: '英検ステップアップ多読：イソップ寓話編 第19巻（準2級 ➔ 2級対比学習・第5集）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第19巻',
    id: 'urn:uuid:e13e4101-0019-4000-8000-000000000019',
    coverImg: 'vol19_cover.jpg',
    koboCoverImg: 'kobo_vol19_cover.jpg',
    fullMdName: 'eiken2_fables_vol19_full.md',
    chapters: [
      { id: 'intro', file: 'vol19_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch41', file: 'vol3_chapter41_old_hound.md', title: '第41話：猟犬と年老いた犬' },
      { id: 'ch42', file: 'vol3_chapter42_wall_and_nail.md', title: '第42話：壁と釘' },
      { id: 'ch43', file: 'vol3_chapter43_fox_and_hedgehog.md', title: '第43話：虻とキツネ' },
      { id: 'ch44', file: 'vol3_chapter44_wild_boar_and_fox.md', title: '第44話：イノシシとキツネ' },
      { id: 'ch45', file: 'vol3_chapter45_astronomer.md', title: '第45話：天文学者' },
      { id: 'ch46', file: 'vol3_chapter46_thief_and_dog.md', title: '第46話：泥棒と見張り番の犬' },
      { id: 'ch47', file: 'vol3_chapter47_lion_and_dolphin.md', title: '第47話：獅子とイルカ' },
      { id: 'ch48', file: 'vol3_chapter48_dog_and_wolf.md', title: '第48話：狼と痩せた犬' },
      { id: 'ch49', file: 'vol3_chapter49_thief_and_his_mother.md', title: '第49話：盗賊と母' },
      { id: 'ch50', file: 'vol3_chapter50_blind_man_and_whelp.md', title: '第50話：盲人と子狼' },
      { id: 'epilogue', file: 'vol19_99_epilogue.md', title: 'おわりに ＆ 次巻のご案内' }
    ]
  },
  {
    num: 20,
    prefix: 'vol20',
    title: '英検ステップアップ多読：イソップ寓話編 第20巻（2級 ➔ 準1級対比学習・第5集）',
    shortTitle: '英検ステップアップ多読：イソップ寓話編 第20巻',
    id: 'urn:uuid:e13e4101-0020-4000-8000-000000000020',
    coverImg: 'vol20_cover.jpg',
    koboCoverImg: 'kobo_vol20_cover.jpg',
    fullMdName: 'eikenPre1_fables_vol20_full.md',
    chapters: [
      { id: 'intro', file: 'vol20_00_introduction.md', title: 'はじめに・構成と学習法' },
      { id: 'ch41', file: 'vol4_chapter41_old_hound.md', title: '第41話：猟犬と年老いた犬' },
      { id: 'ch42', file: 'vol4_chapter42_wall_and_nail.md', title: '第42話：壁と釘' },
      { id: 'ch43', file: 'vol4_chapter43_fox_and_hedgehog.md', title: '第43話：虻とキツネ' },
      { id: 'ch44', file: 'vol4_chapter44_wild_boar_and_fox.md', title: '第44話：イノシシとキツネ' },
      { id: 'ch45', file: 'vol4_chapter45_astronomer.md', title: '第45話：天文学者' },
      { id: 'ch46', file: 'vol4_chapter46_thief_and_dog.md', title: '第46話：泥棒と見張り番の犬' },
      { id: 'ch47', file: 'vol4_chapter47_lion_and_dolphin.md', title: '第47話：獅子とイルカ' },
      { id: 'ch48', file: 'vol4_chapter48_dog_and_wolf.md', title: '第48話：狼と痩せた犬' },
      { id: 'ch49', file: 'vol4_chapter49_thief_and_his_mother.md', title: '第49話：盗賊と母' },
      { id: 'ch50', file: 'vol4_chapter50_blind_man_and_whelp.md', title: '第50話：盲人と子狼' },
      { id: 'epilogue', file: 'vol20_99_epilogue.md', title: 'おわりに ＆ 次巻のご案内' }
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
  console.log(`BUILDING PHASE 5 VOLUME ${vol.num} (${vol.prefix})`);
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
console.log(`ALL PHASE 5 VOLUMES (17, 18, 19, 20) BUILT SUCCESSFULLY!`);
console.log(`========================================\n`);
