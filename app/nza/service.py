from googletrans import Translator
from pypexels import PyPexels
from decouple import config


def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, dest='ru')
    return translation.text


def get_incorrect_answers(obj):
    incorrect_answers = [
        obj.answer_1,
        obj.answer_2,
        obj.answer_3,
        obj.answer_4,
    ]

    correct_answer_index = obj.correct_answer_index - 1
    incorrect_answers.pop(correct_answer_index)
    return incorrect_answers


def get_correct_answer(obj):
    if obj.correct_answer_index == 1:
        return obj.answer_1
    elif obj.correct_answer_index == 2:
        return obj.answer_2
    elif obj.correct_answer_index == 3:
        return obj.answer_3
    elif obj.correct_answer_index == 4:
        return obj.answer_4


class WordTranslateService:
    @staticmethod
    def get_image_url_and_translation(word):
        api_key = config('API_KEY')
        pexel = PyPexels(api_key=api_key)
        search_results = pexel.search(query=word, per_page=1)
        first_result = next(search_results.entries, None)
        image_url = first_result.src['original'] if first_result else None

        translator = Translator()
        translation = translator.translate(word, dest='ru').text

        return translation, image_url