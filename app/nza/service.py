from decouple import config
from nltk.corpus import wordnet
from .models import *
import requests
from googletrans import Translator
from datetime import date
from random import choice
import os


class BaseService:
    model = None

    @classmethod
    def get_current(cls):
        today = date.today()
        current_item = cls.model.objects.filter(date=today).first()

        if current_item is None:
            items = cls.model.objects.all()
            if items:
                item = choice(items)
                current_item = cls.model.objects.create(quote=item, date=today)

        return current_item.quote if current_item else None


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


def get_image_url(self, obj):
    api_key = config('API_KEY')
    url = 'https://api.unsplash.com/photos/random'
    headers = {'Authorization': f'Client-ID {api_key}'}
    params = {'query': obj}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'urls' in data and 'regular' in data['urls']:
                return data['urls']['regular']
        except ValueError:
            print("Ошибка: Невозможно распарсить JSON-данные")

    return 'URL_ПО_УМОЛЧАНИЮ'


def get_translation(self, obj):
    translator = Translator()
    translation = translator.translate(obj, dest='ru')
    return translation.text
class WordTranslateService:
    @staticmethod
    def get_image_url(self, obj):

        api_key = config('API_KEY')
        url = 'https://api.unsplash.com/photos/random'
        headers = {'Authorization': f'Client-ID {api_key}'}
        params = {'query': obj}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data['urls']['regular']


    def get_translation(self, obj):
        translator = Translator()
        translation = translator.translate(obj, dest='ru')
        return translation.text


class GrammarService:
    @staticmethod
    def get_all_grammar():
        return Grammar.objects.all()


class CurrentQuoteService(BaseService):
    model = CurrentQuote


class CurrentIdiomService(BaseService):
    model = CurrentIdiom
