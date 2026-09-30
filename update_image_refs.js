const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;

const stories = [
  'tortoise_and_hare',
  'boy_who_cried_wolf',
  'north_wind_and_sun',
  'lion_and_mouse',
  'ant_and_grasshopper',
  'fox_and_grapes',
  'town_mouse_country_mouse',
  'crow_and_pitcher',
  'dog_and_his_shadow',
  'milkmaid_and_her_pail'
];

const volumeConfigs = [
  { prefix: 'chapter', volPrefix: 'vol1_' },
  { prefix: 'vol2_chapter', volPrefix: 'vol2_' },
  { prefix: 'vol3_chapter', volPrefix: 'vol3_' },
  { prefix: 'vol4_chapter', volPrefix: 'vol4_' }
];

volumeConfigs.forEach(config => {
  const files = fs.readdirSync(kindleDir).filter(f => f.startsWith(config.prefix) && f.endsWith('.md'));
  
  files.forEach(file => {
    const filePath = path.join(kindleDir, file);
    let md = fs.readFileSync(filePath, 'utf8');

    stories.forEach(story => {
      const oldRef = `images/${story}.png`;
      const newRef = `images/${config.volPrefix}${story}.png`;
      md = md.split(oldRef).join(newRef);
    });

    fs.writeFileSync(filePath, md, 'utf8');
    console.log(`Updated image references in ${file} -> ${config.volPrefix}`);
  });
});

console.log('Successfully updated image references across all 40 chapter markdown files.');
