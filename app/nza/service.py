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

class WordTranslateService:
    @staticmethod
    def get_image_url(word):
        api_key = os.environ.get('API_KEY')
        url = 'https://api.unsplash.com/photos/random'
        headers = {'Authorization': f'Client-ID {api_key}'}
        params = {'query': word}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data['urls']['regular']

    @staticmethod
    def get_translation(word):
        translator = Translator()
        translation = translator.translate(word, dest='ru')
        return translation.text


class GrammarService:
    @staticmethod
    def get_all_grammar():
        return Grammar.objects.all()

class CurrentQuoteService(BaseService):
    model = CurrentQuote

class CurrentIdiomService(BaseService):
    model = CurrentIdiom