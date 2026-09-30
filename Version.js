/**
 * Application Version Management
 * 
 * [Changelog]
 * - v1.0.3 (2026-09-30): PWA manifest.json追加 ＆ 全端末（Android, Tablet, Fire, iPhone, iPad）疑似アプリ化ガイドの完全対応
 * - v1.0.2 (2026-09-30): サーバー永続化API（端末変更・キャッシュクリア耐性）、写真直接提出＆親Drive連携、対象級スマートオフライン保存（Cache API）対応
 * - v1.0.1 (2026-09-30): 暗記用マスク機能の強化（物理赤フィルム不要のスマート黒塗り/タップ個別オープン機能に対応）
 * - v1.0.0 (2026-09-30): Initial Release - DAILY HERO & EIKEN STUDIO
 */
const APP_VERSION = "1.0.3";

if (typeof window !== "undefined") {
  window.APP_VERSION = APP_VERSION;
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = { APP_VERSION };
}
