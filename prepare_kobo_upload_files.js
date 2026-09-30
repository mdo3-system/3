const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;
const readyDir = path.join(kindleDir, 'kobo_upload_ready');

if (!fs.existsSync(readyDir)) {
  fs.mkdirSync(readyDir, { recursive: true });
}

const publishingOrder = [
  // フェーズ1: 英検3級を全巻（1〜6巻）
  { step: 1, grade: '英検3級', gradeKey: 'eiken3', gradeVol: 1, internalVol: 1, range: '第1話〜第10話' },
  { step: 2, grade: '英検3級', gradeKey: 'eiken3', gradeVol: 2, internalVol: 5, range: '第11話〜第20話' },
  { step: 3, grade: '英検3級', gradeKey: 'eiken3', gradeVol: 3, internalVol: 9, range: '第21話〜第30話' },
  { step: 4, grade: '英検3級', gradeKey: 'eiken3', gradeVol: 4, internalVol: 13, range: '第31話〜第40話' },
  { step: 5, grade: '英検3級', gradeKey: 'eiken3', gradeVol: 5, internalVol: 17, range: '第41話〜第50話' },
  { step: 6, grade: '英検3級', gradeKey: 'eiken3', gradeVol: 6, internalVol: 21, range: '第51話〜第60話' },

  // フェーズ2: 各級の第1巻
  { step: 7, grade: '英検準2級', gradeKey: 'eikenPre2', gradeVol: 1, internalVol: 2, range: '第1話〜第10話' },
  { step: 8, grade: '英検2級', gradeKey: 'eiken2', gradeVol: 1, internalVol: 3, range: '第1話〜第10話' },
  { step: 9, grade: '英検準1級', gradeKey: 'eikenPre1', gradeVol: 1, internalVol: 4, range: '第1話〜第10話' },

  // フェーズ3: 各級の第2巻
  { step: 10, grade: '英検準2級', gradeKey: 'eikenPre2', gradeVol: 2, internalVol: 6, range: '第11話〜第20話' },
  { step: 11, grade: '英検2級', gradeKey: 'eiken2', gradeVol: 2, internalVol: 7, range: '第11話〜第20話' },
  { step: 12, grade: '英検準1級', gradeKey: 'eikenPre1', gradeVol: 2, internalVol: 8, range: '第11話〜第20話' },

  // フェーズ4: 各級の第3巻
  { step: 13, grade: '英検準2級', gradeKey: 'eikenPre2', gradeVol: 3, internalVol: 10, range: '第21話〜第30話' },
  { step: 14, grade: '英検2級', gradeKey: 'eiken2', gradeVol: 3, internalVol: 11, range: '第21話〜第30話' },
  { step: 15, grade: '英検準1級', gradeKey: 'eikenPre1', gradeVol: 3, internalVol: 12, range: '第21話〜第30話' },

  // フェーズ5: 各級の第4巻
  { step: 16, grade: '英検準2級', gradeKey: 'eikenPre2', gradeVol: 4, internalVol: 14, range: '第31話〜第40話' },
  { step: 17, grade: '英検2級', gradeKey: 'eiken2', gradeVol: 4, internalVol: 15, range: '第31話〜第40話' },
  { step: 18, grade: '英検準1級', gradeKey: 'eikenPre1', gradeVol: 4, internalVol: 16, range: '第31話〜第40話' },

  // フェーズ6: 各級の第5巻
  { step: 19, grade: '英検準2級', gradeKey: 'eikenPre2', gradeVol: 5, internalVol: 18, range: '第41話〜第50話' },
  { step: 20, grade: '英検2級', gradeKey: 'eiken2', gradeVol: 5, internalVol: 19, range: '第41話〜第50話' },
  { step: 21, grade: '英検準1級', gradeKey: 'eikenPre1', gradeVol: 5, internalVol: 20, range: '第41話〜第50話' },

  // フェーズ7: 各級の第6巻（完結）
  { step: 22, grade: '英検準2級', gradeKey: 'eikenPre2', gradeVol: 6, internalVol: 22, range: '第51話〜第60話' },
  { step: 23, grade: '英検2級', gradeKey: 'eiken2', gradeVol: 6, internalVol: 23, range: '第51話〜第60話' },
  { step: 24, grade: '英検準1級', gradeKey: 'eikenPre1', gradeVol: 6, internalVol: 24, range: '第51話〜第60話' }
];

console.log('--- 楽天Kobo (KWL) 出稿用ファイルの整理開始 ---');

publishingOrder.forEach(item => {
  const stepStr = String(item.step).padStart(2, '0');
  const folderName = `${stepStr}_${item.grade}_第${item.gradeVol}巻`;
  const targetSubDir = path.join(readyDir, folderName);

  if (!fs.existsSync(targetSubDir)) {
    fs.mkdirSync(targetSubDir, { recursive: true });
  }

  // 元のepub名
  const srcEpubName = `${item.gradeKey}_fables_vol${item.internalVol}_kobo.epub`;

  // 元のcover名
  let srcCoverName = `kobo_vol${item.internalVol}_cover.jpg`;
  if (!fs.existsSync(path.join(kindleDir, 'images', srcCoverName))) {
    srcCoverName = `vol${item.internalVol}_cover.jpg`;
  }
  if (!fs.existsSync(path.join(kindleDir, 'images', srcCoverName))) {
    if (item.internalVol === 1) srcCoverName = 'cover_kdp.jpg';
    else if (item.internalVol === 2) srcCoverName = 'vol2_cover.jpg';
    else if (item.internalVol === 3) srcCoverName = 'vol3_cover.jpg';
    else if (item.internalVol === 4) srcCoverName = 'vol4_cover.jpg';
  }

  const srcEpubPath = path.join(kindleDir, srcEpubName);
  const srcCoverPath = path.join(kindleDir, 'images', srcCoverName);

  // コピー先ファイル名（一目でわかる名前）
  const destEpubName = `原稿_${item.grade}_第${item.gradeVol}巻.epub`;
  const destCoverName = `表紙_${item.grade}_第${item.gradeVol}巻.jpg`;

  const destEpubPath = path.join(targetSubDir, destEpubName);
  const destCoverPath = path.join(targetSubDir, destCoverName);

  if (fs.existsSync(srcEpubPath)) {
    fs.copyFileSync(srcEpubPath, destEpubPath);
    const sizeMb = (fs.statSync(destEpubPath).size / 1024 / 1024).toFixed(2);
    console.log(`[${stepStr}/24] 配置完了: ${folderName} -> EPUB: ${sizeMb} MB`);
  } else {
    console.warn(`WARNING: EPUB not found: ${srcEpubPath}`);
  }

  if (fs.existsSync(srcCoverPath)) {
    fs.copyFileSync(srcCoverPath, destCoverPath);
  } else {
    console.warn(`WARNING: Cover not found: ${srcCoverPath}`);
  }
});

console.log('SUCCESS: すべての楽天Kobo出稿用ファイルが kobo_upload_ready/ に整理されました！');
