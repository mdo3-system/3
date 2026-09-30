Add-Type -AssemblyName System.Drawing

$dir = Get-Location
$srcPath = Join-Path $dir "images\cover_final.png"
if (-not (Test-Path $srcPath)) {
    $srcPath = Join-Path $dir "images\cover.jpg"
}

$srcImg = [System.Drawing.Image]::FromFile($srcPath)
$targetW = 1600
$targetH = 2560

$canvas = New-Object System.Drawing.Bitmap($targetW, $targetH, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$g = [System.Drawing.Graphics]::FromImage($canvas)

$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

# Royal Navy background (#0A192F)
$bgBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(10, 25, 47))
$g.FillRectangle($bgBrush, 0, 0, $targetW, $targetH)

# Aspect Fit base image
$scaleW = $targetW / $srcImg.Width
$scaleH = $targetH / $srcImg.Height
$scale = [Math]::Min($scaleW, $scaleH)

$drawW = [int]($srcImg.Width * $scale)
$drawH = [int]($srcImg.Height * $scale)
$drawX = [int](($targetW - $drawW) / 2)
$drawY = [int](($targetH - $drawH) / 2)

$g.DrawImage($srcImg, $drawX, $drawY, $drawW, $drawH)

# Overlay top title box for Vol 2
$topBoxBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(200, 10, 25, 47))
$borderPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(244, 208, 111), 6)
$g.FillRectangle($topBoxBrush, 100, 140, 1400, 420)
$g.DrawRectangle($borderPen, 100, 140, 1400, 420)

# Main Title Font
$titleFont = New-Object System.Drawing.Font("Yu Mincho", 46, [System.Drawing.FontStyle]::Bold)
$titleBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 248, 231))
$sfCenter = New-Object System.Drawing.StringFormat
$sfCenter.Alignment = [System.Drawing.StringAlignment]::Center

$g.DrawString("英検ステップアップ多読", $titleFont, $titleBrush, 800, 180, $sfCenter)
$g.DrawString("：イソップ寓話編", $titleFont, $titleBrush, 800, 265, $sfCenter)

# Subtitle Font
$subFont = New-Object System.Drawing.Font("Yu Gothic", 24, [System.Drawing.FontStyle]::Bold)
$subBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(244, 208, 111))
$g.DrawString("3級 ➔ 準2級対比学習で合格レベルの英文力を身につける！", $subFont, $subBrush, 800, 430, $sfCenter)

# Bottom Badge for Vol 2
$badgeBoxBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(240, 10, 25, 47))
$g.FillRectangle($badgeBoxBrush, 420, 2300, 760, 120)
$g.DrawRectangle($borderPen, 420, 2300, 760, 120)

$badgeFont = New-Object System.Drawing.Font("Yu Gothic", 26, [System.Drawing.FontStyle]::Bold)
$badgeBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
$g.DrawString("第2巻（英検準2級受検者向け）", $badgeFont, $badgeBrush, 800, 2335, $sfCenter)

# Save as Vol 2 JPEG
$jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
$encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]98)

$outJpg = Join-Path $dir "images\vol2_cover.jpg"
$canvas.Save($outJpg, $jpegCodec, $encoderParams)

$g.Dispose()
$canvas.Dispose()
$srcImg.Dispose()

Write-Host "SUCCESS: Generated Vol 2 Cover JPEG: $outJpg"
