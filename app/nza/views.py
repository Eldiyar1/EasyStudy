from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Quote, Idiom, Synonym, Antonym, Example, Grammar, Word, Section, Subsection, Listening, Question
from .utils import get_word_translation_and_image_url, \
    perform_word_creation, get_random_idiom_or_quote, create_synonyms_and_antonyms
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
        return get_word_translation_and_image_url(serializer)

    def perform_create(self, serializer):
        perform_word_creation(serializer)

    def get_queryset(self):
        return Word.objects.none()


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializers

    def list(self, request):
        return get_random_idiom_or_quote(self.queryset, self.serializer_class, "Пожалуйста добавьте цитаты")


class IdiomViewSet(ModelViewSet):
    queryset = Idiom.objects.all()
    serializer_class = IdiomSerializers

    def list(self, request):
        return get_random_idiom_or_quote(self.queryset, self.serializer_class, "Пожалуйста добавьте идиому")


class SynonymViewSet(ModelViewSet):
    serializer_class = SynonymSerializer

    def create(self, request, *args, **kwargs):
        synonyms, antonyms = create_synonyms_and_antonyms(request, *args, **kwargs)
        return Response(synonyms, status=201)

    def get_queryset(self):
        return Synonym.objects.none()


class AntonymViewSet(ModelViewSet):
    serializer_class = AntonymSerializer

    def create(self, request, *args, **kwargs):
        synonyms, antonyms = create_synonyms_and_antonyms(request, *args, **kwargs)
        return Response(antonyms, status=201)

    def get_queryset(self):
        return Antonym.objects.none()

class ListeningViewSet(ModelViewSet):
    queryset = Listening.objects.all()
    serializer_class = ListeningSerializer
