const fs = require('fs');
const path = require('path');

const files = [
  '00_introduction.md',
  'chapter01_tortoise_and_hare.md',
  'chapter02_boy_who_cried_wolf.md',
  'chapter03_north_wind_and_sun.md',
  'chapter04_lion_and_mouse.md',
  'chapter05_ant_and_grasshopper.md',
  'chapter06_fox_and_grapes.md',
  'chapter07_town_mouse_country_mouse.md',
  'chapter08_crow_and_pitcher.md',
  'chapter09_dog_and_his_shadow.md',
  'chapter10_milkmaid_and_her_pail.md',
  '99_epilogue_and_next_volume.md'
];

let usedImages = new Set();
usedImages.add('cover.png'); // or cover_kdp.jpg

files.forEach(f => {
  if (fs.existsSync(f)) {
    const text = fs.readFileSync(f, 'utf8');
    const matches = text.match(/images\/([^\s\)\"\'>]+)/g) || [];
    matches.forEach(m => usedImages.add(m.replace('images/', '')));
  }
});

console.log('Count of used images in vol1:', usedImages.size);
let totalSize = 0;
usedImages.forEach(img => {
  const p = path.join('images', img);
  if (fs.existsSync(p)) {
    const size = fs.statSync(p).size;
    totalSize += size;
    console.log(`  ${img}: ${(size / 1024 / 1024).toFixed(2)} MB`);
  } else {
    console.log(`  Missing: ${img}`);
  }
});
console.log('Total size of used images in vol1:', (totalSize / 1024 / 1024).toFixed(2), 'MB');
