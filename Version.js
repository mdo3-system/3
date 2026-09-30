/**
 * Application Version Management
 * 
 * [Changelog]
 * - v1.0.0 (2026-09-30): Initial Release - DAILY HERO & EIKEN STUDIO (全60話イソップ英検スタジオ + 日課クエスト + 資産形成シミュレータ)
 */
const APP_VERSION = "1.0.0";

if (typeof window !== "undefined") {
  window.APP_VERSION = APP_VERSION;
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = { APP_VERSION };
}
