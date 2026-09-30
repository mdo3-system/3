@echo off
chcp 65001 > nul
cls
echo ========================================================
echo   🎬 MDO3出版 英語多読動画 【全自動ビルドシステム】
echo ========================================================
echo.
echo  veo3_inbox に動画を3本入れた状態で実行してください。
echo  自動で結合・音声合成・字幕作成・全6級動画・縦型ショート3本を生成します。
echo.
set /p CH_NUM="ビルドしたい話数（Chapter番号 例: 2 ）を入力してEnter: "
if "%CH_NUM%"=="" set CH_NUM=2

echo.
echo 🚀 Chapter %CH_NUM% の自動ビルドを開始します...
py -3 build_chapter_videos.py %CH_NUM%
py -3 build_integrated_portal.py

echo.
echo ========================================================
echo 🎉 すべての動画ビルドとポータル更新が完了しました！
echo ========================================================
pause
