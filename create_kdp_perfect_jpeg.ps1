Add-Type -AssemblyName System.Drawing

$srcPath = "C:\Users\kokim\.gemini\antigravity-ide\brain\66d672d7-a915-4869-83b9-4644c304d7e9\kindle_cover_portrait_1789892986434.png"
if (-not (Test-Path $srcPath)) {
    $srcPath = Join-Path (Get-Location) "images\cover_final.png"
}

$srcImg = [System.Drawing.Image]::FromFile($srcPath)

$targetW = 1600
$targetH = 2560

# 24bpp RGB Bitmap
$canvas = New-Object System.Drawing.Bitmap($targetW, $targetH, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$g = [System.Drawing.Graphics]::FromImage($canvas)

$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality

# Background fill: Deep dark navy #0D1B2A
$bgBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(13, 27, 42))
$g.FillRectangle($bgBrush, 0, 0, $targetW, $targetH)

# Aspect Fit calculation (0% cropping guaranteed)
$scaleW = $targetW / $srcImg.Width
$scaleH = $targetH / $srcImg.Height
$scale = [Math]::Min($scaleW, $scaleH)

$drawW = [int]($srcImg.Width * $scale)
$drawH = [int]($srcImg.Height * $scale)
$drawX = [int](($targetW - $drawW) / 2)
$drawY = [int](($targetH - $drawH) / 2)

$g.DrawImage($srcImg, $drawX, $drawY, $drawW, $drawH)

$jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
$encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]98)

$outJpg1 = Join-Path (Get-Location) "images\cover_kdp.jpg"
$outJpg2 = Join-Path (Get-Location) "images\cover.jpg"

$canvas.Save($outJpg1, $jpegCodec, $encoderParams)
$canvas.Save($outJpg2, $jpegCodec, $encoderParams)

$g.Dispose()
$canvas.Dispose()
$srcImg.Dispose()

Write-Host "SUCCESS: Created 100% full-view cover (0% cropped) as 1600x2560 JPEG!"
