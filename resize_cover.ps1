Add-Type -AssemblyName System.Drawing
$dir = Get-Location
$pngPath = Join-Path $dir "images\cover_final.png"
$jpgPath = Join-Path $dir "images\cover.jpg"

if (Test-Path $pngPath) {
    $srcImg = [System.Drawing.Image]::FromFile($pngPath)
    $targetWidth = 1600
    $targetHeight = 2560

    $canvas = New-Object System.Drawing.Bitmap($targetWidth, $targetHeight)
    $g = [System.Drawing.Graphics]::FromImage($canvas)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

    $g.DrawImage($srcImg, 0, 0, $targetWidth, $targetHeight)

    $canvas.Save($jpgPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)

    $g.Dispose()
    $canvas.Dispose()
    $srcImg.Dispose()

    Write-Host "SUCCESS: Saved 1600x2560 JPEG as $jpgPath"
}
