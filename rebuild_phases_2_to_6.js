const { execSync } = require('child_process');

console.log('--- REBUILDING ALL PHASES (Phase 2 to 6: Vol 5 to 24) ---');

for (let p = 2; p <= 6; p++) {
  console.log(`\n>>> Processing Phase ${p}...`);
  execSync(`node build_phase${p}_all.js`, { stdio: 'inherit' });
  execSync(`powershell -ExecutionPolicy Bypass -File .\\pack_phase${p}_all.ps1`, { stdio: 'inherit' });
}

console.log('\n--- ALL PHASES REBUILT SUCCESSFULLY! ---');
