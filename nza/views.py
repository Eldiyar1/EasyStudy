from random import choice

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response, APIView
from .models import *
from .serializers import QuoteSerializers, IdiomSerializers, AntonymSerializer, SynonymSerializer, PhotoSerializer, \
    GrammarSerializers
from nltk.corpus import wordnet
import requests


# Create your views here.

class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializers

    def list(self, request):
        quote = choice(self.queryset)
        serializer = self.serializer_class(quote)
        return Response(serializer.data)


class IdiomViewSet(ModelViewSet):
    queryset = Idiom.objects.all()
    serializer_class = IdiomSerializers

    def list(self, request):
        idiom = choice(self.queryset)
        serializer = self.serializer_class(idiom)
        return Response(serializer.data)


class SynonymView(APIView):
    serializer_class = SynonymSerializer

    def post(self, request):
        word = request.data.get('word', '')
        synonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
                if len(synonyms) >= 4:
                    break
            if len(synonyms) >= 4:
                break
        serializer = SynonymSerializer(data={'word': word, 'synonyms': synonyms[:4]})
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class AntonymView(APIView):
    serializer_class = AntonymSerializer

    def post(self, request):
        word = request.data.get('word', '')
        antonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())
                    if len(antonyms) >= 4:
                        break
            if len(antonyms) >= 4:
                break
        serializer = AntonymSerializer(data={'word': word, 'antonyms': antonyms[:4]})
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class PhotoSearchView(APIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, keyword):
        api_key = 'V93q2Wkj7o2bbPNEabw3b0Y3esdVV31pJMpQYbBo4hU  '
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


class GrammarViewSet(ModelViewSet):
    queryset = Grammar.objects.all()
    serializer_class = GrammarSerializers