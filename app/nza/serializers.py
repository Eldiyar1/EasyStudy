from rest_framework import serializers
from .models import Quote, Idiom, Antonym, Synonym, Question, Subsection, Section, Example, Grammar, Word, Listening
from rest_framework.serializers import ModelSerializer
from googletrans import Translator
from .service import WordTranslateService, get_incorrect_answers as get_incorrect_answers_service, \
    get_correct_answer as get_correct_answer_service
from drf_writable_nested import WritableNestedModelSerializer


class ExampleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['id', 'example']


class SubsectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subsection
        fields = ['id', 'subsection', 'section']


class SectionSerializers(serializers.ModelSerializer):
    subsection = SubsectionSerializers(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'section', 'subsection']


class QuestionSerializers(serializers.ModelSerializer):
    incorrect_answers = serializers.SerializerMethodField()
    correct_answer = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'text', 'correct_answer', 'incorrect_answers', 'answer_1', 'answer_2', 'answer_3', 'answer_4',
                  'correct_answer_index')
        extra_kwargs = {
            'answer_1': {'write_only': True},
            'answer_2': {'write_only': True},
            'answer_3': {'write_only': True},
            'answer_4': {'write_only': True},
            'correct_answer_index': {'write_only': True}
        }

    def get_incorrect_answers(self, obj):
        return get_incorrect_answers_service(obj)

    def get_correct_answer(self, obj):
        return get_correct_answer_service(obj)


class GrammarSerializers(WritableNestedModelSerializer, serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        subsection_representation = {
            'id_subsection': instance.subsection.id,
            'subsection': instance.subsection.subsection
        }
        section_representation = {
            'id_section': instance.section.id,
            'section': instance.section.section
        }
        representation.update(section_representation)
        representation.update(subsection_representation)
        return representation

    class Meta:
        model = Grammar
        fields = ['id', 'section', 'subsection', 'title',
                  'description', 'example', 'test']



class WordSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    translation = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        translation, image_url = self.get_translation_and_image_url(obj)
        return image_url

    def get_translation(self, obj):
        translation, _ = self.get_translation_and_image_url(obj)
        return translation

    def get_translation_and_image_url(self, obj):
        service = WordTranslateService()
        return service.get_image_url_and_translation(obj.word)

    class Meta:
        model = Word
        fields = ('id', 'word', 'image_url', 'translation')


class QuoteSerializers(ModelSerializer):
    translation_text = serializers.SerializerMethodField()
    translation_author = serializers.SerializerMethodField()

    def get_translation_text(self, obj):
        translator = Translator()
        translation = translator.translate(obj.text, dest='ru')
        return translation.text

    def get_translation_author(self, obj):
        translator = Translator()
        translation = translator.translate(obj.author, dest='ru')
        return translation.text

    class Meta:
        model = Quote
        fields = ('id', 'text', 'translation_text', 'author', 'translation_author')


class IdiomSerializers(ModelSerializer):
    translation = serializers.SerializerMethodField()

    def get_translation(self, obj):
        translator = Translator()
        translation = translator.translate(obj.text, dest='ru')
        return translation.text

    class Meta:
        model = Idiom
        fields = ('id', 'text', 'translation')


class AntonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antonym
        fields = ('id', 'word', 'antonym')


class SynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
        fields = ('id', 'word', 'synonym')


class ListeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listening
        fields = ('id', 'text')
