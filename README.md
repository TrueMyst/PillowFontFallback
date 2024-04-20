# PillowFontFallback
A script that handles Pillow Font Fallback, a feature that we all wanted.

This is a feature built for [BeatPrints](https://github.com/TrueMyst/BeatPrints) and I do intend to improve this script. I've written this script after seeing this [[Issue #4808]](https://github.com/python-pillow/Pillow/issues/4808). If you think you can improve the script, feel free to open PR.

To get started, run this command.
```bash
pip3 install -r requirements.txt
```

To check it's usage, you can look at the [main.py](https://github.com/TrueMyst/PillowFontFallBack/main.py)

```python
from PIL import Image, ImageDraw
from fontfallback import writing


text_0 = """
My time - Bo en
おやすみ おやすみ
Close your, eyes and you'll leave this dream
おやすみ おやすみ
I know that it's hard to do
"""

text_2 = """
English Text: That's amazing
Arabic Text: هذا مذهل
Korean Text: 그 놀라운
Chinese Simplified: 太棒了
Japanese: すごいですね
"""

fonts = writing.load_fonts(
    "./fonts/Oswald/Oswald-Regular.ttf",
    "./fonts/NotoSansJP/NotoSansJP-Regular.ttf",
    "./fonts/NotoSansKR/NotoSansKR-Regular.ttf",
    "./fonts/NotoSansSC/NotoSansSC-Regular.ttf",
    "./fonts/NotoSansArabic/NotoSansArabic-Regular.ttf",
)

image = Image.new("RGB", (500, 350), color=(255, 255, 255))
draw = ImageDraw.Draw(image)

writing.draw_multiline_text_v2(draw, (40, 10), text_0, (0, 0, 0), fonts, 20)
writing.draw_multiline_text_v2(draw, (40, 150), text_1, (0, 0, 0), fonts, 20)

image.show()
```

Feel free to contribute to this :)
