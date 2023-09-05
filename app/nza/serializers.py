from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer
from googletrans import Translator


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
        fields = ['text', 'translation_text', 'author', 'translation_author']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class IdiomSerializers(ModelSerializer):
    translation = serializers.SerializerMethodField()

    def get_translation(self, obj):
        translator = Translator()
        translation = translator.translate(obj.text, dest='ru')
        return translation.text

    class Meta:
        model = Idiom
        fields = ['text', 'translation']


class AntonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antonym
        fields = ('id', 'word', 'antonym')
        extra_kwargs = {
            'antonym': {'required': False}
        }


class SynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
        fields = ('id', 'word', 'synonym')
        extra_kwargs = {
            'synonym': {'required': False}
        }


class QuestionSerializers(serializers.ModelSerializer):
    incorrect_answers = serializers.SerializerMethodField()
    correct_answer = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('text', 'correct_answer', 'incorrect_answers')

    def get_incorrect_answers(self, obj):
        incorrect_answers = [obj.answer_1, obj.answer_2, obj.answer_3, obj.answer_4, ]
        incorrect_answers.pop(obj.correct_answer_index - 1)
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


class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class SubsectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subsection
        fields = "__all__"


class ExampleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = "__all__"


class GrammarSerializers(serializers.ModelSerializer):
    test = QuestionSerializers(many=True)
    chapter = ChapterSerializers()
    subsection = SubsectionSerializers()

    class Meta:
        model = Grammar
        fields = ('chapter', 'subsection', 'title', 'description', 'test')


class WordSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    translation = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        image_url = "https://api.unsplash.com/photos/random"
        return image_url

    def get_translation(self, obj):
        translator = Translator()
        translation = translator.translate(obj.word, dest='ru')
        return translation.text

    class Meta:
        model = Word
        fields = ['id', 'word', 'image_url', 'translation']
