Add-Type -AssemblyName System.Drawing

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$imgDir = Join-Path $scriptDir "images"

$stories = @(
    "wolf_and_crane",
    "oak_and_reed",
    "horse_and_donkey",
    "bundle_of_sticks",
    "farmer_and_his_sons",
    "frogs_desiring_king",
    "monkey_and_fishermen",
    "lion_in_love",
    "farmer_and_viper",
    "ass_and_lapdog"
)

$vols = @(
    @{
        Prefix = "vol1_"
        Badge = "[ Grade 4 -> Grade 3 Edition ] Target: Eiken Step-Up"
        BgR = 10; BgG = 37; BgB = 64
        BorderR = 52; BorderG = 152; BorderB = 219
        BannerR = 41; BannerG = 128; BannerB = 185
    },
    @{
        Prefix = "vol2_"
        Badge = "[ Grade 3 -> Pre-2 Edition ] Target: Eiken Step-Up"
        BgR = 5; BgG = 41; BgB = 30
        BorderR = 22; BorderG = 160; BorderB = 133
        BannerR = 17; BannerG = 122; BannerB = 101
    },
    @{
        Prefix = "vol3_"
        Badge = "[ Pre-2 -> Grade 2 Edition ] Target: Eiken Step-Up"
        BgR = 45; BgG = 11; BgB = 63
        BorderR = 142; BorderG = 68; BorderB = 173
        BannerR = 108; BannerG = 52; BannerB = 131
    },
    @{
        Prefix = "vol4_"
        Badge = "[ Grade 2 -> Pre-1 Edition ] Target: Eiken Master"
        BgR = 74; BgG = 14; BgB = 23
        BorderR = 192; BorderG = 57; BorderB = 43
        BannerR = 146; BannerG = 43; BannerB = 33
    }
)

foreach ($story in $stories) {
    $srcPath = Join-Path $imgDir ($story + ".png")
    if (-not (Test-Path $srcPath)) {
        Write-Host "WARNING: Source image not found: $srcPath"
        continue
    }

    $srcImg = [System.Drawing.Image]::FromFile($srcPath)

    foreach ($vol in $vols) {
        $targetW = 1200
        $targetH = 1050

        $canvas = New-Object System.Drawing.Bitmap($targetW, $targetH, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
        $g = [System.Drawing.Graphics]::FromImage($canvas)

        $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
        $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

        # Fill Outer Background
        $bgBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb($vol.BgR, $vol.BgG, $vol.BgB))
        $g.FillRectangle($bgBrush, 0, 0, $targetW, $targetH)

        # Draw Outer Border
        $borderPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb($vol.BorderR, $vol.BorderG, $vol.BorderB), 12)
        $g.DrawRectangle($borderPen, 6, 6, $targetW - 12, $targetH - 12)

        # Draw Top Level Badge Banner
        $bannerBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb($vol.BannerR, $vol.BannerG, $vol.BannerB))
        $g.FillRectangle($bannerBrush, 40, 25, $targetW - 80, 75)

        $goldPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(244, 208, 111), 3)
        $g.DrawRectangle($goldPen, 40, 25, $targetW - 80, 75)

        # Badge Text
        $badgeFont = New-Object System.Drawing.Font("Georgia", 20, [System.Drawing.FontStyle]::Bold)
        $whiteBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
        $sfCenter = New-Object System.Drawing.StringFormat
        $sfCenter.Alignment = [System.Drawing.StringAlignment]::Center
        $sfCenter.LineAlignment = [System.Drawing.StringAlignment]::Center

        $g.DrawString($vol.Badge, $badgeFont, $whiteBrush, [float]($targetW / 2), 62.5, $sfCenter)

        # Draw Inner Illustration
        $boxX = 40
        $boxY = 120
        $boxW = 1120
        $boxH = 890

        $scaleW = $boxW / $srcImg.Width
        $scaleH = $boxH / $srcImg.Height
        $scale = [Math]::Min($scaleW, $scaleH)

        $drawW = [int]($srcImg.Width * $scale)
        $drawH = [int]($srcImg.Height * $scale)
        $drawX = $boxX + [int](($boxW - $drawW) / 2)
        $drawY = $boxY + [int](($boxH - $drawH) / 2)

        # Inner Frame Background & Shadow
        $innerBgBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(20, 20, 20))
        $g.FillRectangle($innerBgBrush, $boxX, $boxY, $boxW, $boxH)

        $g.DrawImage($srcImg, $drawX, $drawY, $drawW, $drawH)

        $innerFramePen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb($vol.BorderR, $vol.BorderG, $vol.BorderB), 4)
        $g.DrawRectangle($innerFramePen, $boxX, $boxY, $boxW, $boxH)

        # Save level-specific image PNG
        $outName = $vol.Prefix + $story + ".png"
        $outPath = Join-Path $imgDir $outName
        $canvas.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)

        $g.Dispose()
        $canvas.Dispose()
        Write-Host "Created level illustration: $outName"
    }

    $srcImg.Dispose()
}

Write-Host "SUCCESS: Generated 40 level-tailored illustration PNGs for Phase 4 (chapters 31-40)!"
