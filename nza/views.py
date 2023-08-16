from googletrans import Translator
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response
from .models import *
from .serializers import QuoteSerializers, IdiomSerializers, AntonymSerializer, \
    CategoryWordSerializer, WordSerializer, \
    SynonymSerializer, GrammarSerializers
from nltk.corpus import wordnet
import requests
from rest_framework.decorators import action


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializers

    def list(self, request):
        current_index = request.session.get('current_quote_index', 0)

        if current_index >= len(self.queryset):
            current_index = 0

        quote = self.queryset[current_index]
        serializer = self.serializer_class(quote)

        request.session['current_quote_index'] = (current_index + 1) % len(self.queryset)

        return Response(serializer.data)


class IdiomViewSet(ModelViewSet):
    queryset = Idiom.objects.all()
    serializer_class = IdiomSerializers

    def list(self, request):
        current_index = request.session.get('current_idiom_index', 0)

        if current_index >= len(self.queryset):
            current_index = 0

        quote = self.queryset[current_index]
        serializer = self.serializer_class(quote)

        request.session['current_idiom_index'] = (current_index + 1) % len(self.queryset)

        return Response(serializer.data)


class AntonymViewSet(ModelViewSet):
    serializer_class = AntonymSerializer

    def create(self, request, *args, **kwargs):
        word = request.data.get('word', '')
        antonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())
            if len(antonyms) == 4:
                break
        serializer = self.get_serializer(data={'word': word, 'antonyms': antonyms[:4]})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def get_queryset(self):
        return Antonym.objects.all()


class SynonymViewSet(ModelViewSet):
    serializer_class = SynonymSerializer

    def create(self, request, *args, **kwargs):
        word = request.data.get('word', '')
        synonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
            if len(synonyms) == 4:
                break
        serializer = self.get_serializer(data={'word': word, 'synonym': ', '.join(synonyms[:4])})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def get_queryset(self):
        return Synonym.objects.all()


class CategoryWordViewSet(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = CategoryWordSerializer

    @action(detail=True, methods=['get'])
    def words_by_category(self, request, pk=None):
        words = Word.objects.filter(category=pk)
        serializer = CategoryWordSerializer(words, many=True)
        return Response(serializer.data)


class WordTranslateViewSet(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_image_url(self, word):
        api_key = 'IzKOO2v_sALdUpHkPJcEwFHbbYYW0e0ELBmapfm8NIg'
        url = 'https://api.unsplash.com/photos/random'
        headers = {'Authorization': f'Client-ID {api_key}'}
        params = {'query': word}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data['urls']['regular']

    def get_translation(self, word):
        translator = Translator()
        translation = translator.translate(word, dest='ru')
        return translation.text

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        word_data = serializer.data

        image_url = self.get_image_url(word_data['word'])

        word_translation = self.get_translation(word_data['word'])

        word_data['image_url'] = image_url
        word_data['translation'] = word_translation

        return Response(word_data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        last_word = Word.objects.last()
        new_id = (last_word.id + 1) if last_word else 1
        serializer.save(id=new_id)

    def delete(self, request):
        Word.objects.all().delete()
        Word.objects._reset_sequence(0)


class GrammarViewSet(ModelViewSet):
    queryset = Grammar.objects.all()
    serializer_class = GrammarSerializers

    def list(self, request):
        grammar = Grammar.objects.all()
        serializer = GrammarSerializers(grammar, many=True)
        return Response(serializer.data)
