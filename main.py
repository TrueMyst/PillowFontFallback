from PIL import Image, ImageDraw
from fontfallback import writing

import time

start = time.time()

lyrics = """おやすみ おやすみ
Close your eyes and you'll leave this dream
おやすみ おやすみ
I know that it's hard to do
"""

text_variants = """
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

writing.draw_multiline_text_v2(draw, (40, 30), lyrics, (0, 0, 0), fonts, 20)
writing.draw_multiline_text_v2(draw, (40, 150), text_variants, (0, 0, 0), fonts, 20)

image.show()

end = time.time()
print(end - start)
