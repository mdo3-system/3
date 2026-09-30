Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$baseLoc = Get-Location

$vols = @(
    @{
        Prefix = "vol13"
        KdpZip = "eiken3_fables_vol13_kdp.zip"
        EpubBase = "eiken3_fables_vol13"
    },
    @{
        Prefix = "vol14"
        KdpZip = "eikenPre2_fables_vol14_kdp.zip"
        EpubBase = "eikenPre2_fables_vol14"
    },
    @{
        Prefix = "vol15"
        KdpZip = "eiken2_fables_vol15_kdp.zip"
        EpubBase = "eiken2_fables_vol15"
    },
    @{
        Prefix = "vol16"
        KdpZip = "eikenPre1_fables_vol16_kdp.zip"
        EpubBase = "eikenPre1_fables_vol16"
    }
)

function Pack-Epub-Strict ($buildDirName, $outFileName, $lang) {
    $opfPath = Join-Path $baseLoc "$buildDirName\OEBPS\content.opf"
    $opfContent = [System.IO.File]::ReadAllText($opfPath, [System.Text.Encoding]::UTF8)
    if ($lang -eq "ja") {
        $opfContent = $opfContent.Replace("<dc:language>en</dc:language>", "<dc:language>ja</dc:language>")
    } else {
        $opfContent = $opfContent.Replace("<dc:language>ja</dc:language>", "<dc:language>en</dc:language>")
    }
    [System.IO.File]::WriteAllText($opfPath, $opfContent, [System.Text.Encoding]::UTF8)

    $zipPath = Join-Path $baseLoc $outFileName
    if (Test-Path $zipPath) { Remove-Item $zipPath -Force }

    $zipStream = [System.IO.File]::Create($zipPath)
    $archive = New-Object System.IO.Compression.ZipArchive($zipStream, [System.IO.Compression.ZipArchiveMode]::Create)

    # 1. mimetype FIRST (Uncompressed)
    $mimeEntry = $archive.CreateEntry("mimetype", [System.IO.Compression.CompressionLevel]::NoCompression)
    $writer = New-Object System.IO.StreamWriter($mimeEntry.Open(), [System.Text.Encoding]::ASCII)
    $writer.Write("application/epub+zip")
    $writer.Dispose()

    # 2. Other files with Optimal compression
    $fullBuildDir = Join-Path $baseLoc $buildDirName
    $files = Get-ChildItem -Recurse $fullBuildDir | Where-Object { -not $_.PSIsContainer -and $_.Name -ne "mimetype" }
    foreach ($file in $files) {
        $relativePath = $file.FullName.Substring($fullBuildDir.Length + 1).Replace("\", "/")
        $entry = $archive.CreateEntry($relativePath, [System.IO.Compression.CompressionLevel]::Optimal)
        $entryStream = $entry.Open()
        $fileStream = [System.IO.File]::OpenRead($file.FullName)
        $fileStream.CopyTo($entryStream)
        $fileStream.Dispose()
        $entryStream.Dispose()
    }

    $archive.Dispose()
    $zipStream.Dispose()
    Write-Host "Created strict EPUB ($lang): $outFileName"
}

foreach ($v in $vols) {
    Write-Host "=== Packaging $($v.Prefix) ==="

    # 1. Pack KDP ZIP
    $zipBuildDir = Join-Path $baseLoc "$($v.Prefix)_kdp_zip_build"
    $kdpZipPath = Join-Path $baseLoc $v.KdpZip
    if (Test-Path $kdpZipPath) { Remove-Item $kdpZipPath -Force }
    [System.IO.Compression.ZipFile]::CreateFromDirectory($zipBuildDir, $kdpZipPath)
    Write-Host "Packed KDP ZIP: $($v.KdpZip)"

    # 2. Pack EPUBs (en and ja)
    $epubDir = "$($v.Prefix)_epub_build"
    $epubEn = "$($v.EpubBase).epub"
    $epubJa = "$($v.EpubBase)_ja.epub"
    $epubKobo = "$($v.EpubBase)_kobo.epub"

    Pack-Epub-Strict $epubDir $epubEn "en"
    Pack-Epub-Strict $epubDir $epubJa "ja"

    # 3. Create Kobo EPUB
    Copy-Item (Join-Path $baseLoc $epubJa) (Join-Path $baseLoc $epubKobo) -Force
    Write-Host "Created Rakuten Kobo EPUB: $epubKobo"
}

Write-Host "SUCCESS: All Phase 4 packages (Kindle KDP ZIP, Kindle EPUB, Kobo EPUB) generated!"
