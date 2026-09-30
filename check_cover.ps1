Add-Type -AssemblyName System.Drawing

$imgFinal = [System.Drawing.Image]::FromFile((Join-Path (Get-Location) "images\cover_final.png"))
Write-Host "cover_final.png Width:" $imgFinal.Width "Height:" $imgFinal.Height
$imgFinal.Dispose()

$imgBase = [System.Drawing.Image]::FromFile((Join-Path (Get-Location) "images\cover.png"))
Write-Host "cover.png Width:" $imgBase.Width "Height:" $imgBase.Height
$imgBase.Dispose()
