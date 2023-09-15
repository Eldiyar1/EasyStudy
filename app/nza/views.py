from random import choice
from rest_framework.views import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Quote, Idiom, Synonym, Antonym, Example, Grammar, Word, Section, Subsection, Listening, Question
from .service import get_synonyms, get_antonyms
from .serializers import QuoteSerializers, IdiomSerializers, AntonymSerializer, WordSerializer, SynonymSerializer, \
    GrammarSerializers, ExampleSerializers, SectionSerializers, SubsectionSerializers, ListeningSerializer, \
    QuestionSerializers


class SectionViewSet(ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


class SubsectionViewSet(ModelViewSet):
    queryset = Subsection.objects.all()
    serializer_class = SubsectionSerializers


class GrammarViewSet(ModelViewSet):
    queryset = Grammar.objects.all()
    serializer_class = GrammarSerializers


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers


class ExampleViewSet(ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializers


class WordTranslateViewSet(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        word_data = serializer.data

        word_translation, image_url = serializer.get_translation_and_image_url(instance)

        word_data['image_url'] = image_url
        word_data['translation'] = word_translation

        return Response(word_data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        last_word = Word.objects.last()
        new_id = (last_word.id + 1) if last_word else 1
        serializer.save(id=new_id)

    def get_queryset(self):
        return Word.objects.none()


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializers

    def list(self, request):
        if self.queryset:
            quote = choice(self.queryset)
            serializer = self.serializer_class(quote)
            return Response(serializer.data)
        else:
            return Response({"Ошибка": "Пожалуйста добавьте цитаты"})


class IdiomViewSet(ModelViewSet):
    queryset = Idiom.objects.all()
    serializer_class = IdiomSerializers

    def list(self, request):
        if self.queryset:
            idiom = choice(self.queryset)
            serializer = self.serializer_class(idiom)
            return Response(serializer.data)
        else:
            return Response({"Ошибка": "Пожалуйста добавьте идиомы"})


class SynonymViewSet(ModelViewSet):
    serializer_class = SynonymSerializer

    def create(self, request, *args, **kwargs):
        word = request.data.get('word', '')
        synonyms = get_synonyms(word)

        synonym_list = [{'word': word, 'synonym': synonym} for synonym in synonyms]

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
        antonyms = get_antonyms(word)

        antonym_list = [{'word': word, 'antonym': antonym} for antonym in antonyms]

        serializer = self.get_serializer(data=antonym_list, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def get_queryset(self):
        return Antonym.objects.none()


class ListeningViewSet(ModelViewSet):
    queryset = Listening.objects.all()
    serializer_class = ListeningSerializer
