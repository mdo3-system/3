Add-Type -AssemblyName System.Drawing
$dir = Get-Location
$pngPath = Join-Path $dir "images\cover_final.png"
$jpgPath = Join-Path $dir "images\cover.jpg"
Write-Host "Target PNG: $pngPath"
if (Test-Path $pngPath) {
    $img = [System.Drawing.Image]::FromFile($pngPath)
    $img.Save($jpgPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
    $img.Dispose()
    Write-Host "SUCCESS: Saved JPEG as $jpgPath"
} else {
    Write-Host "ERROR: File not found $pngPath"
}
