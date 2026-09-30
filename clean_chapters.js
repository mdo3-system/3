const fs = require('fs');
const path = require('path');

const kindleDir = __dirname;
const chapters = [
  'chapter01_tortoise_and_hare.md',
  'chapter02_boy_who_cried_wolf.md',
  'chapter03_north_wind_and_sun.md',
  'chapter04_lion_and_mouse.md',
  'chapter05_ant_and_grasshopper.md',
  'chapter06_fox_and_grapes.md',
  'chapter07_town_mouse_country_mouse.md',
  'chapter08_crow_and_pitcher.md',
  'chapter09_dog_and_his_shadow.md',
  'chapter10_milkmaid_and_her_pail.md'
];

chapters.forEach(file => {
  const filePath = path.join(kindleDir, file);
  if (!fs.existsSync(filePath)) return;

  let text = fs.readFileSync(filePath, 'utf8');

  // Remove ## 1. Visual Illustration Spec... section completely up to the first ---
  // Pattern: ## 1. Visual Illustration Spec[\s\S]*?(?=\n---\n)
  text = text.replace(/## 1\. Visual Illustration Spec[\s\S]*?\n---\n/g, '');

  // Re-number remaining sections:
  // ## 2. Benchmark Level -> ## 1. Benchmark Level: Eiken Grade 4 (英検4級レベル本文)
  // ## 3. Target Level -> ## 2. Target Level: Eiken Grade 3 (英検3級レベル本文)
  // ## 4. Classic Original -> ## 3. Classic Original English Text (イソップ寓話 クラシック原文)
  // ## 5. Japanese Translation -> ## 4. Japanese Translation (日本語訳)
  // ## 6. Recite & Compare -> ## 5. Recite & Compare (そらんじたいキーフレーズ対比表)
  // ## 7. Key Vocabulary & Exam Notes -> ## 6. Key Vocabulary & Exam Notes (語彙・文法・試験対策解説)

  text = text.replace(/## 2\. Benchmark Level/g, '## 1. Benchmark Level');
  text = text.replace(/## 3\. Target Level/g, '## 2. Target Level');
  text = text.replace(/## 4\. Classic Original/g, '## 3. Classic Original');
  text = text.replace(/## 5\. Japanese Translation/g, '## 4. Japanese Translation');
  text = text.replace(/## 6\. Recite & Compare/g, '## 5. Recite & Compare');
  text = text.replace(/## 7\. Key Vocabulary/g, '## 6. Key Vocabulary');

  fs.writeFileSync(filePath, text, 'utf8');
  console.log(`Cleaned prompt section from: ${file}`);
});
