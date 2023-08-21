from nltk.corpus import wordnet
from .models import *
import requests
from googletrans import Translator
from decouple import config
from datetime import date
from random import choice


class CurrentQuoteService:
    @staticmethod
    def get_current_quote():
        today = date.today()
        current_quote = CurrentQuote.objects.filter(date=today).first()

        if current_quote is None:
            quote = choice(Quote.objects.all())
            current_quote = CurrentQuote.objects.create(quote=quote, date=today)

        return current_quote.quote


class CurrentIdiomService:
    @staticmethod
    def get_current_idiom():
        today = date.today()
        current_idiom = CurrentIdiom.objects.filter(date=today).first()

        if current_idiom is None:
            idiom = choice(Idiom.objects.all())
            current_idiom = CurrentIdiom.objects.create(idiom=idiom, date=today)

        return current_idiom.idiom


class AntonymService:
    @staticmethod
    def get_antonyms(word, num_antonyms=4):
        antonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())
            if len(antonyms) >= num_antonyms:
                break
        return antonyms


class WordTranslateService:
    @staticmethod
    def get_image_url(word):
        api_key = config('API_KEY')
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
