Add-Type -AssemblyName System.Drawing

$imgDir = Join-Path $PSScriptRoot "images"
if (-not (Test-Path $imgDir)) {
    New-Item -ItemType Directory -Path $imgDir | Out-Null
}

$stories = @(
    @{
        Key = "honest_woodcutter"
        TitleEn = "The Honest Woodcutter"
        TitleJa = "金の斧と銀の斧"
        Perry = "Perry 173"
        Moral = "Honesty is the best policy"
        Symbol = "🪓 ✨ 🌊"
        ColorTop = [System.Drawing.Color]::FromArgb(15, 32, 67)
        ColorBottom = [System.Drawing.Color]::FromArgb(35, 75, 120)
        Accent = [System.Drawing.Color]::FromArgb(241, 196, 15)
    },
    @{
        Key = "goose_golden_eggs"
        TitleEn = "The Goose that Laid the Golden Eggs"
        TitleJa = "金の卵を産むガチョウ"
        Perry = "Perry 87"
        Moral = "Greed destroys the source of wealth"
        Symbol = "🪿 🥚 ✨"
        ColorTop = [System.Drawing.Color]::FromArgb(44, 30, 10)
        ColorBottom = [System.Drawing.Color]::FromArgb(100, 75, 25)
        Accent = [System.Drawing.Color]::FromArgb(243, 156, 18)
    },
    @{
        Key = "wolf_in_sheeps_clothing"
        TitleEn = "The Wolf in Sheep's Clothing"
        TitleJa = "羊の皮をかぶった狼"
        Perry = "Perry 451"
        Moral = "Appearances can be deceptive"
        Symbol = "🐺 🐑 🌙"
        ColorTop = [System.Drawing.Color]::FromArgb(26, 26, 36)
        ColorBottom = [System.Drawing.Color]::FromArgb(60, 60, 80)
        Accent = [System.Drawing.Color]::FromArgb(231, 76, 60)
    },
    @{
        Key = "fox_and_stork"
        TitleEn = "The Fox and the Stork"
        TitleJa = "キツネとツル"
        Perry = "Perry 426"
        Moral = "One bad turn deserves another"
        Symbol = "🦊 🦩 🏺"
        ColorTop = [System.Drawing.Color]::FromArgb(40, 20, 10)
        ColorBottom = [System.Drawing.Color]::FromArgb(90, 50, 25)
        Accent = [System.Drawing.Color]::FromArgb(230, 126, 34)
    },
    @{
        Key = "frog_and_ox"
        TitleEn = "The Frog and the Ox"
        TitleJa = "カエルと牛"
        Perry = "Perry 376"
        Moral = "Self-conceit leads to destruction"
        Symbol = "🐸 🐂 💨"
        ColorTop = [System.Drawing.Color]::FromArgb(15, 35, 20)
        ColorBottom = [System.Drawing.Color]::FromArgb(35, 80, 45)
        Accent = [System.Drawing.Color]::FromArgb(46, 204, 113)
    },
    @{
        Key = "bat_birds_beasts"
        TitleEn = "The Bat, Birds, and Beasts"
        TitleJa = "コウモリと鳥と獣"
        Perry = "Perry 566"
        Moral = "He that is friend to all is friend to none"
        Symbol = "🦇 🦅 🦁"
        ColorTop = [System.Drawing.Color]::FromArgb(20, 15, 35)
        ColorBottom = [System.Drawing.Color]::FromArgb(50, 40, 85)
        Accent = [System.Drawing.Color]::FromArgb(155, 89, 182)
    },
    @{
        Key = "belling_the_cat"
        TitleEn = "Belling the Cat"
        TitleJa = "ネズミの会議"
        Perry = "Perry 613"
        Moral = "Easy to propose, hard to execute"
        Symbol = "🐭 🔔 🐱"
        ColorTop = [System.Drawing.Color]::FromArgb(25, 25, 30)
        ColorBottom = [System.Drawing.Color]::FromArgb(65, 60, 65)
        Accent = [System.Drawing.Color]::FromArgb(241, 196, 15)
    },
    @{
        Key = "bear_and_two_travelers"
        TitleEn = "The Bear and the Travelers"
        TitleJa = "旅人とクマ"
        Perry = "Perry 65"
        Moral = "Misfortune tests true friendship"
        Symbol = "🐻 🌲 🚶"
        ColorTop = [System.Drawing.Color]::FromArgb(30, 20, 15)
        ColorBottom = [System.Drawing.Color]::FromArgb(75, 50, 35)
        Accent = [System.Drawing.Color]::FromArgb(211, 84, 0)
    },
    @{
        Key = "lions_share"
        TitleEn = "The Lion's Share"
        TitleJa = "獅子の分け前"
        Perry = "Perry 149"
        Moral = "Might makes right"
        Symbol = "🦁 👑 🦌"
        ColorTop = [System.Drawing.Color]::FromArgb(45, 15, 15)
        ColorBottom = [System.Drawing.Color]::FromArgb(105, 35, 30)
        Accent = [System.Drawing.Color]::FromArgb(244, 208, 111)
    },
    @{
        Key = "frog_and_mouse"
        TitleEn = "The Frog and the Mouse"
        TitleJa = "ネズミとカエル"
        Perry = "Perry 384"
        Moral = "Harm set, harm get"
        Symbol = "🐸 🧵 🐭"
        ColorTop = [System.Drawing.Color]::FromArgb(10, 35, 40)
        ColorBottom = [System.Drawing.Color]::FromArgb(25, 80, 90)
        Accent = [System.Drawing.Color]::FromArgb(26, 188, 156)
    }
)

$w = 1024
$h = 1024

foreach ($s in $stories) {
    $bmp = New-Object System.Drawing.Bitmap($w, $h, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $g = [System.Drawing.Graphics]::FromImage($bmp)

    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

    # Draw Linear Gradient Background
    $rect = New-Object System.Drawing.Rectangle(0, 0, $w, $h)
    $gradient = New-Object System.Drawing.Drawing2D.LinearGradientBrush($rect, $s.ColorTop, $s.ColorBottom, [System.Drawing.Drawing2D.LinearGradientMode]::ForwardDiagonal)
    $g.FillRectangle($gradient, $rect)

    # Double Ornate Border
    $penGoldOuter = New-Object System.Drawing.Pen($s.Accent, 10)
    $penGoldInner = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(180, $s.Accent.R, $s.Accent.G, $s.Accent.B), 3)
    $g.DrawRectangle($penGoldOuter, 25, 25, $w - 50, $h - 50)
    $g.DrawRectangle($penGoldInner, 40, 40, $w - 80, $h - 80)

    # Corner Accents
    $cornerSize = 50
    $brushAccent = New-Object System.Drawing.SolidBrush($s.Accent)
    $g.FillPolygon($brushAccent, @(
        (New-Object System.Drawing.PointF(40, 40)),
        (New-Object System.Drawing.PointF(40 + $cornerSize, 40)),
        (New-Object System.Drawing.PointF(40, 40 + $cornerSize))
    ))
    $g.FillPolygon($brushAccent, @(
        (New-Object System.Drawing.PointF($w - 40, 40)),
        (New-Object System.Drawing.PointF($w - 40 - $cornerSize, 40)),
        (New-Object System.Drawing.PointF($w - 40, 40 + $cornerSize))
    ))
    $g.FillPolygon($brushAccent, @(
        (New-Object System.Drawing.PointF(40, $h - 40)),
        (New-Object System.Drawing.PointF(40 + $cornerSize, $h - 40)),
        (New-Object System.Drawing.PointF(40, $h - 40 - $cornerSize))
    ))
    $g.FillPolygon($brushAccent, @(
        (New-Object System.Drawing.PointF($w - 40, $h - 40)),
        (New-Object System.Drawing.PointF($w - 40 - $cornerSize, $h - 40)),
        (New-Object System.Drawing.PointF($w - 40, $h - 40 - $cornerSize))
    ))

    # Center Ellipse Glow
    $centerBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(40, 255, 255, 255))
    $g.FillEllipse($centerBrush, 160, 260, $w - 320, 400)

    # Alignment Format
    $sf = New-Object System.Drawing.StringFormat
    $sf.Alignment = [System.Drawing.StringAlignment]::Center
    $sf.LineAlignment = [System.Drawing.StringAlignment]::Center

    # Perry Badge at Top
    $fontPerry = New-Object System.Drawing.Font("Georgia", 22, [System.Drawing.FontStyle]::Bold)
    $g.DrawString("AESOP'S FABLES • " + $s.Perry, $fontPerry, $brushAccent, [float]($w / 2), 110, $sf)

    # Decorative Line
    $penLine = New-Object System.Drawing.Pen($s.Accent, 2)
    $g.DrawLine($penLine, 200, 145, $w - 200, 145)

    # Central Symbol / Emojis / Art Token
    $fontSymbol = New-Object System.Drawing.Font("Segoe UI Emoji", 70, [System.Drawing.FontStyle]::Regular)
    $brushWhite = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
    $g.DrawString($s.Symbol, $fontSymbol, $brushWhite, [float]($w / 2), 340, $sf)

    # Main English Title
    $fontTitle = New-Object System.Drawing.Font("Georgia", 36, [System.Drawing.FontStyle]::Bold)
    $layoutRectEn = New-Object System.Drawing.RectangleF(70, 490, $w - 140, 160)
    $g.DrawString($s.TitleEn, $fontTitle, $brushWhite, $layoutRectEn, $sf)

    # Japanese Subtitle
    $fontJa = New-Object System.Drawing.Font("Yu Mincho", 32, [System.Drawing.FontStyle]::Bold)
    $brushGold = New-Object System.Drawing.SolidBrush($s.Accent)
    $g.DrawString("（" + $s.TitleJa + "）", $fontJa, $brushGold, [float]($w / 2), 700, $sf)

    # Moral Banner Box
    $moralRect = New-Object System.Drawing.RectangleF(80, 800, $w - 160, 90)
    $brushMoralBg = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(160, 0, 0, 0))
    $g.FillRectangle($brushMoralBg, $moralRect)
    $g.DrawRectangle($penLine, $moralRect.X, $moralRect.Y, $moralRect.Width, $moralRect.Height)

    $fontMoral = New-Object System.Drawing.Font("Georgia", 20, [System.Drawing.FontStyle]::Italic)
    $brushMoralText = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(240, 240, 240))
    $g.DrawString("Moral: " + $s.Moral, $fontMoral, $brushMoralText, [float]($w / 2), 845, $sf)

    # Save PNG
    $outPath = Join-Path $imgDir ($s.Key + ".png")
    $bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)

    $g.Dispose()
    $bmp.Dispose()
    Write-Host "Created base illustration plate: $($s.Key).png"
}

Write-Host "SUCCESS: Generated all 10 base illustration plates in images/!"
