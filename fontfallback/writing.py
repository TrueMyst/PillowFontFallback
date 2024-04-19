import re
from PIL import ImageFont, ImageDraw
from lingua import Language, LanguageDetectorBuilder

from . import utils


def process_language(text: str):
    """
    Detects languages, and puts them into a list with their assigned language code
    """
    characters = []

    # It wouldn't be practical to use all the langauges. So I only added some of them
    detector = LanguageDetectorBuilder.from_languages(
        Language.ENGLISH,
        Language.KOREAN,
        Language.JAPANESE,
        Language.CHINESE,
        Language.ARABIC,
        Language.BENGALI,
        Language.HINDI,
    ).build()

    sentences = re.split(r"(\s+)", text)

    # Connectives, here is being refered to Script/Cursive languages, feel free to add more to your liking.
    # Make sure to add them to the detector as well.
    connective_languages = {Language.ARABIC, Language.BENGALI, Language.HINDI}

    for word in sentences:
        lang = detector.detect_language_of(word)

        if lang in connective_languages:
            characters.append([word, str(lang.iso_code_639_1.name).lower()])
        else:
            for char in word:
                if char.isspace():
                    characters.append([char, None])

                elif char in utils.punctuations:
                    characters.append([char, "en"])

                elif char.isalnum():
                    try:
                        detected = str(lang.iso_code_639_1.name).lower()
                    except:
                        detected = "unknown"
                    characters.append([char, detected])

    return characters


def draw_text(
    draw: ImageDraw.ImageDraw,
    cords: tuple,
    text: str,
    size: int,
    color: tuple,
    path: dict,
):
    """
    Draw a single line text.
    """
    offset = 0
    sentence = process_language(text)

    for char, detect_lang in sentence:
        cords_ = (cords[0] + offset, cords[1])

        font_info = path.get(detect_lang, path["en"])
        font_path = font_info.get("path")

        font = ImageFont.truetype(font_path, size)
        draw.text(cords_, char, color, font)

        box = font.getbbox(char)
        offset += box[2] - box[0]


def draw_multitext(
    draw: ImageDraw.ImageDraw,
    cords: tuple,
    text: str,
    size: int,
    color: tuple,
    path: dict,
    spacing=0,
):
    """
    Draw a multi-line line text.
    """
    spacing = cords[1]
    lines = text.split("\n")

    for line in lines:
        mod_cord = (cords[0], spacing)
        draw_text(draw, mod_cord, line, size, color, path)

        spacing += size + 5
