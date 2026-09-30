Add-Type -AssemblyName System.Drawing

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$imgDir = Join-Path $scriptDir "images"

$srcPath = Join-Path $imgDir "cover_final.png"
if (-not (Test-Path $srcPath)) {
    $srcPath = Join-Path $imgDir "cover.png"
}
$srcImg = [System.Drawing.Image]::FromFile($srcPath)

$jsonPath = Join-Path $scriptDir "covers_config_phase6.json"
$jsonRaw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
$covers = ConvertFrom-Json $jsonRaw

$targetW = 1600
$targetH = 2560

$jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
$encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]98)

foreach ($c in $covers) {
    $canvas = New-Object System.Drawing.Bitmap($targetW, $targetH, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
    $g = [System.Drawing.Graphics]::FromImage($canvas)

    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

    # Fill theme background
    $bgBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb($c.BgR, $c.BgG, $c.BgB))
    $g.FillRectangle($bgBrush, 0, 0, $targetW, $targetH)

    # Fit source image
    $scaleW = $targetW / $srcImg.Width
    $scaleH = $targetH / $srcImg.Height
    $scale = [Math]::Min($scaleW, $scaleH)

    $drawW = [int]($srcImg.Width * $scale)
    $drawH = [int]($srcImg.Height * $scale)
    $drawX = [int](($targetW - $drawW) / 2)
    $drawY = [int](($targetH - $drawH) / 2)

    $g.DrawImage($srcImg, $drawX, $drawY, $drawW, $drawH)

    # Draw Bottom Badge Banner
    $badgeRect = New-Object System.Drawing.Rectangle(150, 2260, 1300, 140)
    $badgeBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(230, 13, 27, 42))
    $g.FillRectangle($badgeBrush, $badgeRect)

    $goldPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(244, 208, 111), 6)
    $g.DrawRectangle($goldPen, $badgeRect)

    $sf = New-Object System.Drawing.StringFormat
    $sf.Alignment = [System.Drawing.StringAlignment]::Center
    $sf.LineAlignment = [System.Drawing.StringAlignment]::Center

    $badgeFont = New-Object System.Drawing.Font("Yu Gothic", 36, [System.Drawing.FontStyle]::Bold)
    $whiteBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
    $g.DrawString($c.Badge, $badgeFont, $whiteBrush, [float]800, [float]2330, $sf)

    # Save outputs
    $outPath = Join-Path $imgDir $c.OutName
    $canvas.Save($outPath, $jpegCodec, $encoderParams)

    $koboPath = Join-Path $imgDir $c.KoboName
    $canvas.Save($koboPath, $jpegCodec, $encoderParams)

    $g.Dispose()
    $canvas.Dispose()
    Write-Host "Created cover JPEG: $($c.OutName) and $($c.KoboName)"
}

$srcImg.Dispose()
Write-Host "SUCCESS: Generated all covers for Vol 21, 22, 23, 24!"
