const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;

const mdFiles = fs.readdirSync(kindleDir).filter(f => f.endsWith('.md'));

console.log(`--- Clean MD files for Rakuten Kobo & KDP compliance (${mdFiles.length} files) ---`);

let totalModified = 0;

mdFiles.forEach(file => {
  const filePath = path.join(kindleDir, file);
  let content = fs.readFileSync(filePath, 'utf8');
  let original = content;

  // 1. Amazon direct URLs & Links
  content = content.replace(/https:\/\/www\.amazon\.co\.jp\/dp\/[^\s"')]+/g, '');
  content = content.replace(/https:\/\/www\.amazon\.co\.jp[^\s"')]+/g, '');

  // 2. Platform specific text
  content = content.replace(/Amazonで第(\d+)巻をチェックする（ワンクリックで購入・閲覧）/g, '各電子書籍ストアにて第$1巻も好評配信中！');
  content = content.replace(/\[Amazon著者ページ \/ シリーズストアへ\]\(\)/g, '');
  content = content.replace(/Amazon著者ページ \/ シリーズストアへ/g, '電子書籍ストアシリーズ一覧');
  content = content.replace(/Amazonのカスタマーレビュー/g, '電子書籍ストアのカスタマーレビュー');
  content = content.replace(/Amazon Kindle/g, '電子書籍');
  content = content.replace(/Kindle Voice \(TTS\)/g, '音声読み上げ機能 (TTS)');
  content = content.replace(/Kindle Voice/g, '音声読み上げ機能 (TTS)');
  content = content.replace(/Kindle TTS/g, '音声読み上げ機能 (TTS)');
  content = content.replace(/Kindleの読み上げ機能/g, '音声読み上げ機能');
  content = content.replace(/Kindleの朗読/g, '電子書籍の朗読');
  content = content.replace(/Kindle/g, '電子書籍');

  // 3. Emojis removal/replacement
  content = content.replace(/💡/g, '【ポイント】');
  content = content.replace(/📌/g, '■');
  content = content.replace(/🚀/g, '');
  content = content.replace(/👉/g, '・');
  content = content.replace(/🌟/g, '■');
  content = content.replace(/📖/g, '■');
  content = content.replace(/🎯/g, '■');
  content = content.replace(/📚/g, '■');

  // Clean empty href tag or broken a tags if any
  content = content.replace(/<a href=""[^>]*>\s*・?\s*<\/a>/g, '');

  if (content !== original) {
    fs.writeFileSync(filePath, content, 'utf8');
    totalModified++;
    console.log(`Updated: ${file}`);
  }
});

console.log(`Done! Modified ${totalModified} / ${mdFiles.length} markdown files.`);
