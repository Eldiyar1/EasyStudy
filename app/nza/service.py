from nltk.corpus import wordnet
from .models import *
from datetime import date
from googletrans import Translator
from pypexels import PyPexels
from decouple import config


def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
        if len(synonyms) == 4:
            break
    return synonyms[:4]


def get_antonyms(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
        if len(antonyms) == 4:
            break
    return antonyms[:4]


class GrammarService:
    @staticmethod
    def get_all_grammar():
        return Grammar.objects.all()


class BaseService:
    model = None

    @classmethod
    def get_current(cls):
        today = date.today()
        current_item = cls.model.objects.filter(date=today).first()

        return current_item.quote if current_item else None


class CurrentQuoteService(BaseService):
    model = CurrentQuote


class CurrentIdiomService(BaseService):
    model = CurrentIdiom

class WordTranslateService:
    @staticmethod
    def get_image_url_and_translation(word):
        api_key = config('API_KEY')
        py_pexel = PyPexels(api_key=api_key)
        search_results = py_pexel.search(query=word, per_page=1)
        first_result = next(search_results.entries, None)
        image_url = first_result.src['original'] if first_result else None

        translator = Translator()
        translation = translator.translate(word, dest='ru').text

        return translation, image_url