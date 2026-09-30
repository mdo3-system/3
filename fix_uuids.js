const fs = require('fs');

const files = [
  'build_phase2_all.js',
  'build_phase3_all.js',
  'build_phase4_all.js',
  'build_phase5_all.js',
  'build_phase6_all.js'
];

files.forEach(f => {
  if (fs.existsSync(f)) {
    let content = fs.readFileSync(f, 'utf8');
    // Replace id: 'urn:uuid:...' with a valid RFC 4122 UUID
    content = content.replace(/id:\s*'urn:uuid:[^']+'/g, (match) => {
      // Find volume number from context or extract
      return match;
    });

    // Specifically replace each known invalid UUID pattern
    for (let v = 5; v <= 24; v++) {
      const vPad = String(v).padStart(2, '0');
      const validUuid = `urn:uuid:e13e4101-00${vPad}-4000-8000-0000000000${vPad}`;
      const reg = new RegExp(`urn:uuid:[a-zA-Z0-9]+-fables-vol${v}-2026`, 'g');
      content = content.replace(reg, validUuid);
    }

    fs.writeFileSync(f, content, 'utf8');
    console.log(`Updated UUIDs in ${f}`);
  }
});
