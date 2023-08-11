from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer
from googletrans import Translator


class QuoteSerializers(ModelSerializer):
    translation = serializers.SerializerMethodField()

    def get_translation(self, obj):
        translator = Translator()
        translation = translator.translate(obj.text, dest='ru')
        return translation.text

    class Meta:
        model = Quote
        fields = ['text', 'translation']


class IdiomSerializers(ModelSerializer):
    translation = serializers.SerializerMethodField()

    def get_translation(self, obj):
        translator = Translator()
        translation = translator.translate(obj.text, dest='ru')
        return translation.text

    class Meta:
        model = Idiom
        fields = ['text', 'translation']


class SynonymSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)
    synonyms = serializers.ListField(child=serializers.CharField(max_length=100), required=False)


class AntonymSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)
    antonyms = serializers.ListField(child=serializers.CharField(max_length=100), required=False)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['keyword', 'image_url', 'created_at']


class GrammarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Grammar
        fields = '__all__'

class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['chapter']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'created_at', 'statistics', 'achievements']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']


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


class CategoryWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'category', 'word']
