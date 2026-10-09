/**
 * Google Apps Script (GAS) - Google Drive Auto-Upload Webhook for Daiki Portal
 * 
 * [設置手順]
 * 1. Google Drive (お父様のアカウント) を開き、新規 -> その他 -> Google Apps Script を作成。
 * 2. このコードを貼り付けてプロジェクト名を「DaikiPortal_DriveSync」などに設定。
 * 3. 画面右上の「デプロイ」->「新しいデプロイ」をクリック。
 * 4. 種類の選択: 「ウェブアプリ」
 *    - 次のユーザーとして実行: 「自分」
 *    - アクセスできるユーザー: 「全員」
 * 5. デプロイ後、発行された「ウェブアプリURL (https://script.google.com/macros/s/.../exec)」をコピー。
 * 6. config/portal_config.json の "googleDriveUploadWebhookUrl" にそのURLを貼り付けます。
 */

function doPost(e) {
  try {
    var data;
    if (e.postData.type === "application/json") {
      data = JSON.parse(e.postData.contents);
    } else {
      data = e.parameter;
    }

    var base64Data = data.base64;
    var filename = data.filename || ("daiki_" + Utilities.formatDate(new Date(), "Asia/Tokyo", "yyyyMMdd_HHmmss") + ".jpg");
    var subject = data.subject || "general";
    var folderName = "daiki";

    if (!base64Data) {
      return ContentService.createTextOutput(JSON.stringify({
        status: "error",
        message: "No base64 data provided"
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // 1. "daiki" フォルダの取得または新規作成
    var folders = DriveApp.getFoldersByName(folderName);
    var targetFolder;
    if (folders.hasNext()) {
      targetFolder = folders.next();
    } else {
      targetFolder = DriveApp.createFolder(folderName);
    }

    // 日付別サブフォルダ (例: 2026-10) を作成して整理
    var subFolderName = Utilities.formatDate(new Date(), "Asia/Tokyo", "yyyy-MM");
    var subFolders = targetFolder.getFoldersByName(subFolderName);
    var monthFolder;
    if (subFolders.hasNext()) {
      monthFolder = subFolders.next();
    } else {
      monthFolder = targetFolder.createFolder(subFolderName);
    }

    // 2. Base64デコードして画像を保存
    var decoded = Utilities.base64Decode(base64Data);
    var contentType = data.contentType || "image/jpeg";
    var blob = Utilities.newBlob(decoded, contentType, filename);
    var file = monthFolder.createFile(blob);

    // 閲覧権限を「リンクを知っている全員が閲覧可」に設定（アプリ内の高速プレビュー用）
    file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);

    var fileId = file.getId();
    var viewUrl = "https://drive.google.com/uc?export=view&id=" + fileId;
    var directUrl = file.getUrl();
    var downloadUrl = file.getDownloadUrl();
    var thumbnailUrl = "https://drive.google.com/thumbnail?id=" + fileId + "&sz=w600";

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      fileId: fileId,
      filename: filename,
      folder: folderName + "/" + subFolderName,
      viewUrl: viewUrl,
      directUrl: directUrl,
      thumbnailUrl: thumbnailUrl,
      uploadedAt: Utilities.formatDate(new Date(), "Asia/Tokyo", "yyyy-MM-dd HH:mm:ss")
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({
    status: "online",
    service: "Daiki Portal Google Drive Webhook",
    timestamp: new Date().toISOString()
  })).setMimeType(ContentService.MimeType.JSON);
}
