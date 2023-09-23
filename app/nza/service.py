from googletrans import Translator
from pypexels import PyPexels
from decouple import config

from app.nza.constants import DESTINATION_LANGUAGE


def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, dest=DESTINATION_LANGUAGE)
    return translation.text


def get_incorrect_answers(obj):
    incorrect_answers = [getattr(obj, f'answer_{i}') for i in range(1, 5)]
    incorrect_answers.pop(obj.correct_answer_index - 1)
    return incorrect_answers


def get_correct_answer(obj):
    answers = {1: obj.answer_1, 2: obj.answer_2, 3: obj.answer_3, 4: obj.answer_4}
    return answers.get(obj.correct_answer_index)


class WordTranslateService:
    @staticmethod
    def get_image_url_and_translation(word, destination_language=DESTINATION_LANGUAGE):
        api_key = config('API_KEY')
        pexel = PyPexels(api_key=api_key)
        search_results = pexel.search(query=word, per_page=1)
        first_result = next(search_results.entries, None)
        image_url = first_result.src['medium'] if first_result else None

        translator = Translator()
        translation = translator.translate(word, dest=destination_language).text

        return translation, image_url