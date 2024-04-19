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


# Example usage
image = Image.new("RGB", (500, 230), color=(255, 255, 255))
draw = ImageDraw.Draw(image)
language_dict = {
    "en": {"path": "./fonts/Oswald/Oswald-Regular.ttf"},
    "ko": {"path": "./fonts/NotoSansKR/NotoSansKR-Regular.ttf"},
    "ja": {"path": "./fonts/NotoSansJP/NotoSansJP-Regular.ttf"},
    "zh": {"path": "./fonts/NotoSansSC/NotoSansSC-Regular.ttf"},
    "ar": {"path": "./fonts/NotoSansArabic/NotoSansArabic-Regular.ttf"},
    # Add hindi and bengali fonts here
}

text1 = """おやすみ おやすみ
Close your, eyes and you'll leave this dream
おやすみ おやすみ
I know that it's hard to do
"""

text2 = "Goodbye وداعا さようなら 안녕히 계세요 再见"

writing.draw_text(draw, (10, 130), text2, 20, (0, 0, 0), language_dict)
writing.draw_multitext(draw, (10, 10), text1, 20, (0, 0, 0), language_dict)

image.show()

```

Feel free to contribute :)
