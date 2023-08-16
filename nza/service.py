from django.contrib.sessions.models import Session
from nltk.corpus import wordnet
from .models import Word
from .models import Grammar
import requests
from googletrans import Translator


class QuoteService:
    @staticmethod
    def get_current_quote(request, queryset):
        current_index = request.session.get('current_quote_index', 0)

        if current_index >= len(queryset):
            current_index = 0

        quote = queryset[current_index]
        request.session['current_quote_index'] = (current_index + 1) % len(queryset)

        return quote


class IdiomService:
    @staticmethod
    def get_current_idiom(request, queryset):
        current_index = request.session.get('current_idiom_index', 0)

        if current_index >= len(queryset):
            current_index = 0

        idiom = queryset[current_index]
        request.session['current_idiom_index'] = (current_index + 1) % len(queryset)

        return idiom



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
        api_key = 'IzKOO2v_sALdUpHkPJcEwFHbbYYW0e0ELBmapfm8NIg'
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

