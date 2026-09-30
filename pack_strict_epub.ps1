Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

function Pack-Epub ($outFileName, $lang) {
    $opfPath = Join-Path (Get-Location) "epub_build\OEBPS\content.opf"
    $opfContent = [System.IO.File]::ReadAllText($opfPath)
    if ($lang -eq "ja") {
        $opfContent = $opfContent.Replace("<dc:language>en</dc:language>", "<dc:language>ja</dc:language>")
    } else {
        $opfContent = $opfContent.Replace("<dc:language>ja</dc:language>", "<dc:language>en</dc:language>")
    }
    [System.IO.File]::WriteAllText($opfPath, $opfContent)

    $zipPath = Join-Path (Get-Location) $outFileName
    if (Test-Path $zipPath) { Remove-Item $zipPath -Force }

    $zipStream = [System.IO.File]::Create($zipPath)
    $archive = New-Object System.IO.Compression.ZipArchive($zipStream, [System.IO.Compression.ZipArchiveMode]::Create)

    # 1. mimetype FIRST (Uncompressed / NoCompression)
    $mimeEntry = $archive.CreateEntry("mimetype", [System.IO.Compression.CompressionLevel]::NoCompression)
    $writer = New-Object System.IO.StreamWriter($mimeEntry.Open(), [System.Text.Encoding]::ASCII)
    $writer.Write("application/epub+zip")
    $writer.Dispose()

    # 2. Other files with Optimal compression
    $baseDir = Join-Path (Get-Location) "epub_build"
    $files = Get-ChildItem -Recurse $baseDir | Where-Object { -not $_.PSIsContainer -and $_.Name -ne "mimetype" }
    foreach ($file in $files) {
        $relativePath = $file.FullName.Substring($baseDir.Length + 1).Replace("\", "/")
        $entry = $archive.CreateEntry($relativePath, [System.IO.Compression.CompressionLevel]::Optimal)
        $entryStream = $entry.Open()
        $fileStream = [System.IO.File]::OpenRead($file.FullName)
        $fileStream.CopyTo($entryStream)
        $fileStream.Dispose()
        $entryStream.Dispose()
    }

    $archive.Dispose()
    $zipStream.Dispose()
    Write-Host "SUCCESS: Built strictly compliant EPUB ($lang) -> $outFileName"
}

node make_epub_strict.js
Pack-Epub "eiken3_fables_vol1.epub" "en"
Pack-Epub "eiken3_fables_vol1_ja.epub" "ja"
