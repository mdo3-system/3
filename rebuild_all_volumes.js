const { execSync } = require('child_process');

console.log('--- REBUILDING ALL 4 VOLUMES WITH LEVEL-TAILORED ILLUSTRATIONS ---');

console.log('[1/4] Rebuilding Volume 1 (Grade 4 -> Grade 3)...');
execSync('node build_kdp_zip.js', { stdio: 'inherit' });
execSync('powershell -ExecutionPolicy Bypass -File .\\pack_strict_epub.ps1', { stdio: 'inherit' });

console.log('[2/4] Rebuilding Volume 2 (Grade 3 -> Pre-2)...');
execSync('node build_vol2.js', { stdio: 'inherit' });
execSync('node make_vol2_epub.js', { stdio: 'inherit' });
execSync('powershell -ExecutionPolicy Bypass -File .\\pack_vol2_all.ps1', { stdio: 'inherit' });

console.log('[3/4] Rebuilding Volume 3 (Pre-2 -> Grade 2)...');
execSync('node build_vol3.js', { stdio: 'inherit' });
execSync('node make_vol3_epub.js', { stdio: 'inherit' });
execSync('powershell -ExecutionPolicy Bypass -File .\\pack_vol3_all.ps1', { stdio: 'inherit' });

console.log('[4/4] Rebuilding Volume 4 (Grade 2 -> Pre-1)...');
execSync('node build_vol4.js', { stdio: 'inherit' });
execSync('node make_vol4_epub.js', { stdio: 'inherit' });
execSync('powershell -ExecutionPolicy Bypass -File .\\pack_vol4_all.ps1', { stdio: 'inherit' });

console.log('SUCCESS: All 4 Volumes fully rebuilt with level-tailored illustrations and EPUB/ZIP packages!');
