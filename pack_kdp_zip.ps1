node build_kdp_zip.js

$zipPath = Join-Path (Get-Location) "eiken3_fables_vol1_kdp.zip"
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }

Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::CreateFromDirectory("kdp_zip_build", $zipPath)

Write-Host "SUCCESS: Generated Amazon KDP native HTML/ZIP manuscript: $zipPath"
