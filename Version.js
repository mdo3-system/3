/**
 * Application Version Management
 * 
 * [Changelog]
 * - v1.0.1 (2026-09-30): 暗記用マスク機能の強化（物理赤フィルム不要のスマート黒塗り/タップ個別オープン機能に対応）
 * - v1.0.0 (2026-09-30): Initial Release - DAILY HERO & EIKEN STUDIO
 */
const APP_VERSION = "1.0.1";

if (typeof window !== "undefined") {
  window.APP_VERSION = APP_VERSION;
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = { APP_VERSION };
}
