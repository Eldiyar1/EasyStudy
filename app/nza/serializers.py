from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import Quote, Idiom, Antonym, Synonym, Question, Subsection, Section, Example, Grammar, Word, Listening
from rest_framework.serializers import ModelSerializer
from .service import WordTranslateService, get_incorrect_answers as get_incorrect_answers_service, \
    get_correct_answer as get_correct_answer_service, translate_text


class ExampleSerializers(serializers.ModelSerializer):
    grammar_id = serializers.PrimaryKeyRelatedField(
        queryset=Grammar.objects.all(), source='grammar', write_only=True)

    class Meta:
        model = Example
        fields = ['id', 'grammar_id', 'example']


class QuestionSerializers(serializers.ModelSerializer):
    incorrect_answers = serializers.SerializerMethodField()
    correct_answer = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'grammar', 'text', 'correct_answer', 'incorrect_answers', 'answer_1', 'answer_2', 'answer_3',
                  'answer_4', 'correct_answer_index')
        extra_kwargs = {
            'grammar': {'write_only': True},
            'answer_1': {'write_only': True},
            'answer_2': {'write_only': True},
            'answer_3': {'write_only': True},
            'answer_4': {'write_only': True},
            'correct_answer_index': {'write_only': True}
        }

    @staticmethod
    def get_incorrect_answers(obj):
        return get_incorrect_answers_service(obj)

    @staticmethod
    def get_correct_answer(obj):
        return get_correct_answer_service(obj)


class GrammarListSerializers(WritableNestedModelSerializer, serializers.ModelSerializer):
    question = QuestionSerializers(many=True, read_only=True)
    example = ExampleSerializers(many=True, read_only=True)

    class Meta:
        model = Grammar
        fields = ['id', 'subsection', 'title', 'description', 'example', 'question']
        extra_kwargs = {
            'subsection': {'write_only': True},
        }


class GrammarSerializers(serializers.ModelSerializer):
    example = ExampleSerializers(many=True, read_only=True)

    class Meta:
        model = Grammar
        fields = ['id', 'title', 'description', 'example']


class SubsectionListSerializers(serializers.ModelSerializer):
    grammar = GrammarSerializers(many=True, read_only=True)
    example = ExampleSerializers(many=True, read_only=True)

    class Meta:
        model = Subsection
        fields = ['id', 'section', 'subsection', 'grammar', 'example']
        extra_kwargs = {
            'section': {'write_only': True},
        }


class SubsectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subsection
        fields = ['id', 'subsection']


class SectionListSerializers(serializers.ModelSerializer):
    subsection = SubsectionSerializers(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'section', 'subsection']


class WordSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    translation = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        translation, image_url = self.get_translation_and_image_url(obj)
        return image_url

    def get_translation(self, obj):
        translation, _ = self.get_translation_and_image_url(obj)
        return translation

    @staticmethod
    def get_translation_and_image_url(obj):
        service = WordTranslateService()
        return service.get_image_url_and_translation(obj.word)

    class Meta:
        model = Word
        fields = ('id', 'word', 'image_url', 'translation')


class QuoteSerializers(ModelSerializer):
    translation_text = serializers.SerializerMethodField()
    translation_author = serializers.SerializerMethodField()

    @staticmethod
    def get_translation_text(obj):
        return translate_text(obj.text)

    @staticmethod
    def get_translation_author(obj):
        return translate_text(obj.author)

    class Meta:
        model = Quote
        fields = ('id', 'text', 'translation_text', 'author', 'translation_author')


class IdiomSerializers(ModelSerializer):
    translation = serializers.SerializerMethodField()

    @staticmethod
    def get_translation(obj):
        return translate_text(obj.text)

    class Meta:
        model = Idiom
        fields = ('id', 'text', 'translation')


class AntonymSerializer(serializers.ModelSerializer):
    antonym = serializers.ReadOnlyField()

    class Meta:
        model = Antonym
        fields = ('id', 'word', 'antonym')


class SynonymSerializer(serializers.ModelSerializer):
    synonym = serializers.ReadOnlyField()

    class Meta:
        model = Synonym
        fields = ('id', 'word', 'synonym')


class ListeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listening
        fields = ('id', 'text')
