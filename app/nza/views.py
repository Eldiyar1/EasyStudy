from rest_framework.decorators import action
from rest_framework.views import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .service import *
from .serializers import QuoteSerializers, \
    IdiomSerializers, AntonymSerializer, \
    WordSerializer, SynonymSerializer, \
    CategorySerializer, GrammarSerializers,\
    ExampleSerializers


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializers

    def list(self, request):
        current_quote = CurrentQuoteService.get_current()
        serializer = self.serializer_class(current_quote)
        return Response(serializer.data)


class IdiomViewSet(ModelViewSet):
    queryset = Idiom.objects.all()
    serializer_class = IdiomSerializers

    def list(self, request):
        current_idiom = CurrentIdiomService.get_current()
        serializer = self.serializer_class(current_idiom)
        return Response(serializer.data)


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

        synonym_list = [{'word': word, 'synonym': synonym} for synonym in synonyms[:4]]

        serializer = self.get_serializer(data=synonym_list, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def get_queryset(self):
        return Synonym.objects.none()


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

        antonym_list = [{'word': word, 'antonym': antonym} for antonym in antonyms[:4]]

        serializer = self.get_serializer(data=antonym_list, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def get_queryset(self):
        return Antonym.objects.none()


class WordTranslateViewSet(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        word_data = serializer.data

        image_url = WordTranslateService.get_image_url(word_data['word'])

        word_translation = WordTranslateService.get_translation(word_data['word'])

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

class ExampleViewSet(ModelViewSet):
    queryset = ExampleSerializers
    serializer_class = Example.objects.all()

class GrammarViewSet(ModelViewSet):
    queryset = Grammar.objects.all()
    serializer_class = GrammarSerializers

    def list(self, request, *args, **kwargs):
        grammar = GrammarService.get_all_grammar()
        serializer = self.serializer_class(grammar, many=True)
        return Response(serializer.data)


class CategoryWordViewSet(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def words_by_category(self, request, pk=None):
        words = Word.objects.filter(category=pk)
        serializer = CategorySerializer(words, many=True)
        return Response(serializer.data)
