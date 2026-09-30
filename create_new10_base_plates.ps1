Add-Type -AssemblyName System.Drawing

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$imgDir = Join-Path $scriptDir "images"
if (-not (Test-Path $imgDir)) {
    New-Item -ItemType Directory -Path $imgDir | Out-Null
}

$jsonPath = Join-Path $scriptDir "new10_stories.json"
$jsonRaw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
$stories = ConvertFrom-Json $jsonRaw

[int]$w = 1024
[int]$h = 1024

foreach ($s in $stories) {
    $bmp = New-Object System.Drawing.Bitmap($w, $h, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $g = [System.Drawing.Graphics]::FromImage($bmp)

    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

    $cTop = [System.Drawing.Color]::FromArgb($s.ColorTop[0], $s.ColorTop[1], $s.ColorTop[2])
    $cBottom = [System.Drawing.Color]::FromArgb($s.ColorBottom[0], $s.ColorBottom[1], $s.ColorBottom[2])
    $cAccent = [System.Drawing.Color]::FromArgb($s.Accent[0], $s.Accent[1], $s.Accent[2])

    # Background gradient
    $rect = New-Object System.Drawing.Rectangle(0, 0, $w, $h)
    $gradient = New-Object System.Drawing.Drawing2D.LinearGradientBrush($rect, $cTop, $cBottom, [System.Drawing.Drawing2D.LinearGradientMode]::ForwardDiagonal)
    $g.FillRectangle($gradient, $rect)

    # Double Ornate Border
    $penGoldOuter = New-Object System.Drawing.Pen($cAccent, 10)
    $penGoldInner = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(180, $cAccent.R, $cAccent.G, $cAccent.B), 3)
    $g.DrawRectangle($penGoldOuter, 25, 25, $w - 50, $h - 50)
    $g.DrawRectangle($penGoldInner, 40, 40, $w - 80, $h - 80)

    # Corner Accents
    $cornerSize = 50
    $brushAccent = New-Object System.Drawing.SolidBrush($cAccent)
    
    [System.Drawing.Point[]]$pts1 = @(
        (New-Object System.Drawing.Point(40, 40)),
        (New-Object System.Drawing.Point(40 + $cornerSize, 40)),
        (New-Object System.Drawing.Point(40, 40 + $cornerSize))
    )
    $g.FillPolygon($brushAccent, $pts1)

    [System.Drawing.Point[]]$pts2 = @(
        (New-Object System.Drawing.Point($w - 40, 40)),
        (New-Object System.Drawing.Point($w - 40 - $cornerSize, 40)),
        (New-Object System.Drawing.Point($w - 40, 40 + $cornerSize))
    )
    $g.FillPolygon($brushAccent, $pts2)

    [System.Drawing.Point[]]$pts3 = @(
        (New-Object System.Drawing.Point(40, $h - 40)),
        (New-Object System.Drawing.Point(40 + $cornerSize, $h - 40)),
        (New-Object System.Drawing.Point(40, $h - 40 - $cornerSize))
    )
    $g.FillPolygon($brushAccent, $pts3)

    [System.Drawing.Point[]]$pts4 = @(
        (New-Object System.Drawing.Point($w - 40, $h - 40)),
        (New-Object System.Drawing.Point($w - 40 - $cornerSize, $h - 40)),
        (New-Object System.Drawing.Point($w - 40, $h - 40 - $cornerSize))
    )
    $g.FillPolygon($brushAccent, $pts4)

    # Center glow
    $centerBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(40, 255, 255, 255))
    $g.FillEllipse($centerBrush, 160, 260, $w - 320, 400)

    $sf = New-Object System.Drawing.StringFormat
    $sf.Alignment = [System.Drawing.StringAlignment]::Center
    $sf.LineAlignment = [System.Drawing.StringAlignment]::Center

    # Perry badge
    $fontPerry = New-Object System.Drawing.Font("Georgia", 22, [System.Drawing.FontStyle]::Bold)
    $perryText = "AESOP'S FABLES - " + $s.Perry
    $g.DrawString($perryText, $fontPerry, $brushAccent, [float]($w / 2), [float]110, $sf)

    # Divider line
    $penLine = New-Object System.Drawing.Pen($cAccent, 2)
    $g.DrawLine($penLine, 200, 145, $w - 200, 145)

    # Symbol token
    $fontSymbol = New-Object System.Drawing.Font("Georgia", 30, [System.Drawing.FontStyle]::Bold)
    $brushWhite = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
    $g.DrawString($s.Symbol, $fontSymbol, $brushAccent, [float]($w / 2), [float]330, $sf)

    # Main English Title
    $fontTitle = New-Object System.Drawing.Font("Georgia", 34, [System.Drawing.FontStyle]::Bold)
    $rectTitle = New-Object System.Drawing.RectangleF([float]70, [float]470, [float]($w - 140), [float]180)
    $g.DrawString($s.TitleEn, $fontTitle, $brushWhite, $rectTitle, $sf)

    # Japanese Subtitle
    $fontJa = New-Object System.Drawing.Font("Yu Mincho", 32, [System.Drawing.FontStyle]::Bold)
    $brushGold = New-Object System.Drawing.SolidBrush($cAccent)
    $jaText = "(" + $s.TitleJa + ")"
    $g.DrawString($jaText, $fontJa, $brushGold, [float]($w / 2), [float]700, $sf)

    # Moral Banner Box
    [int]$mx = 80
    [int]$my = 800
    [int]$mw = $w - 160
    [int]$mh = 90
    $brushMoralBg = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(180, 0, 0, 0))
    $g.FillRectangle($brushMoralBg, $mx, $my, $mw, $mh)
    $g.DrawRectangle($penLine, $mx, $my, $mw, $mh)

    $fontMoral = New-Object System.Drawing.Font("Georgia", 20, [System.Drawing.FontStyle]::Italic)
    $brushMoralText = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(240, 240, 240))
    $moralStr = "Moral: " + $s.Moral
    $g.DrawString($moralStr, $fontMoral, $brushMoralText, [float]($w / 2), [float]845, $sf)

    # Save PNG
    $outName = $s.Key + ".png"
    $outPath = Join-Path $imgDir $outName
    $bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)

    $g.Dispose()
    $bmp.Dispose()
    Write-Host "Created base illustration plate: $outName"
}

Write-Host "SUCCESS: Generated all 10 base illustration plates in images/!"
