from rest_framework import serializers
from .models import Quote, Idiom, Antonym, Synonym, Question, Subsection, Section, Example, Grammar, Word, Listening
from rest_framework.serializers import ModelSerializer
from googletrans import Translator
from .service import WordTranslateService


class ExampleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['id', 'example']


class SectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'section', 'subsection')


class SubsectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subsection
        fields = ['id', 'subsection']


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
        incorrect_answers = [
            obj.answer_1,
            obj.answer_2,
            obj.answer_3,
            obj.answer_4,
        ]

        correct_answer_index = obj.correct_answer_index - 1
        incorrect_answers.pop(correct_answer_index)
        return incorrect_answers

    def get_correct_answer(self, obj):
        if obj.correct_answer_index == 1:
            return obj.answer_1
        elif obj.correct_answer_index == 2:
            return obj.answer_2
        elif obj.correct_answer_index == 3:
            return obj.answer_3
        elif obj.correct_answer_index == 4:
            return obj.answer_4


class GrammarSerializers(serializers.ModelSerializer):
    test = QuestionSerializers(many=True)
    section = SectionSerializers()
    example = ExampleSerializers(many=True)

    class Meta:
        model = Grammar
        fields = ['id', 'section', 'title', 'description', 'example', 'test']


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
