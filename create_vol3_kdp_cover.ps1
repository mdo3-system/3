Add-Type -AssemblyName System.Drawing

$srcPath = Join-Path (Get-Location) "images\cover_final.png"
if (-not (Test-Path $srcPath)) {
    $srcPath = Join-Path (Get-Location) "images\cover.png"
}

$srcImg = [System.Drawing.Image]::FromFile($srcPath)

$targetW = 1600
$targetH = 2560

$canvas = New-Object System.Drawing.Bitmap($targetW, $targetH, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$g = [System.Drawing.Graphics]::FromImage($canvas)

$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality

# Background fill: Royal Purple for Vol 3 / Grade 2 (#2D0B3F)
$bgBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(45, 11, 63))
$g.FillRectangle($bgBrush, 0, 0, $targetW, $targetH)

# Aspect Fit calculation
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

$outJpg = Join-Path (Get-Location) "images\vol3_cover.jpg"
$canvas.Save($outJpg, $jpegCodec, $encoderParams)

$g.Dispose()
$canvas.Dispose()
$srcImg.Dispose()

Write-Host "SUCCESS: Created Vol 3 Cover as 1600x2560 JPEG: $outJpg"
