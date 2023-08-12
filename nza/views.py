from random import choice

from django.shortcuts import get_object_or_404
from googletrans import Translator
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response, APIView
from .models import *
from .serializers import QuoteSerializers, IdiomSerializers, AntonymSerializer, SynonymSerializer, PhotoSerializer, \
    GrammarSerializers, CategoryWordSerializer, WordSerializer, \
    ChapterSerializers, QuestionSerializers
from nltk.corpus import wordnet
import requests
from rest_framework.decorators import action


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializers
    def list(self, request):
        quote = choice(self.queryset)
        serializer = self.serializer_class(quote)
        return Response(serializer.data)
    # def list(self, request):
    #     quote_index = request.session.get('quote_index', 0)
    #     quote = get_object_or_404(self.queryset, pk=quote_index + 1)
    #
    #     request.session['quote_index'] = (quote_index + 1) % len(self.queryset)
    #
    #     return Response(self.serializer_class(quote).data)


class IdiomViewSet(ModelViewSet):
    queryset = Idiom.objects.all()
    serializer_class = IdiomSerializers


    def list(self, request):
        idiom_index = request.session.get('idiom_index', 0)
        idiom = get_object_or_404(self.queryset, pk=idiom_index + 1)

        request.session['idiom_index'] = (idiom_index + 1) % len(self.queryset)

        return Response(self.serializer_class(idiom).data)


class AntonymView(APIView):
    serializer_class = AntonymSerializer

    def post(self, request):
        word = request.data.get('word', '')
        antonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())
            if len(antonyms) == 4:
                break
        serializer = AntonymSerializer(data={'word': word, 'antonyms': antonyms[:4]})
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class SynonymView(APIView):
    serializer_class = SynonymSerializer

    def post(self, request):
        word = request.data.get('word', '')
        synonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
            if len(synonyms) == 4:
                break
        serializer = SynonymSerializer(data={'word': word, 'synonyms': synonyms[:4]})
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)




class PhotoSearchView(APIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, keyword):
        api_key = 'V93q2Wkj7o2bbPNEabw3b0Y3esdVV31pJMpQYbBo4hU'
        url = 'https://api.unsplash.com/photos/random'

        headers = {
            'Authorization': f'Client-ID {api_key}'
        }

        params = {
            'query': keyword
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        photo_data = {
            'keyword': keyword,
            'image_url': data['urls']['regular']
        }

        serializer = self.serializer_class(data=photo_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class GrammarViewSet(APIView):
    def get(self, request):
        grammar = Grammar.objects.all()
        serializer = GrammarSerializers(grammar, many=True)
        return Response(serializer.data)


class ChapterViewSet(ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializers

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






class QuestionListView(APIView):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        serializer = QuestionSerializers(questions, many=True)
        return Response(serializer.data)
