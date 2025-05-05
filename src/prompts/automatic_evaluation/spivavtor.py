from src.prompts.base_prompts import BasePrompt

spivavtor_gec_verbalizers: list[str] = [
    "Виправте граматику в цьому реченнi:",
    "Виправте граматичнi помилки в цьому реченнi:",
    "Удосконалiть граматику цього тексту:",
    "Виправте всi граматичнi помилки:",
    "Зробiть речення граматичним:",
    "Видалiть граматичнi помилки:",
    "Виправте помилки в цьому текстi:",
    "Виправте граматичнi помилки:",
    "Виправити граматику:",
]


class SpivavtorGECPrompt(BasePrompt):
    template: str = """{verbalizer} {original_text}"""

    input_variables: list[str] = ["verbalizer", "original_text"]
