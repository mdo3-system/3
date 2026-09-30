const fs = require('fs');
const path = require('path');

const baseDir = __dirname;
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

let fullMarkdown = '';

files.forEach(file => {
  const filePath = path.join(baseDir, file);
  if (fs.existsSync(filePath)) {
    console.log(`Processing: ${file}`);
    const content = fs.readFileSync(filePath, 'utf8');
    fullMarkdown += content + '\n\n<div style="page-break-before: always;"></div>\n\n';
  } else {
    console.warn(`Warning: File not found: ${file}`);
  }
});

// Save combined markdown
const outputPath = path.join(baseDir, 'eiken3_fables_vol1_full.md');
fs.writeFileSync(outputPath, fullMarkdown, 'utf8');
console.log(`Successfully compiled full book into: ${outputPath}`);
