const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;
const buildDir = path.join(kindleDir, 'epub_build');
const oebpsDir = path.join(buildDir, 'OEBPS');

// Read content.opf and change <dc:language>en</dc:language> to <dc:language>ja</dc:language>
const opfPath = path.join(oebpsDir, 'content.opf');
let opfText = fs.readFileSync(opfPath, 'utf8');
opfText = opfText.replace('<dc:language>en</dc:language>', '<dc:language>ja</dc:language>');
fs.writeFileSync(opfPath, opfText, 'utf8');

console.log('Updated content.opf to language: ja');
