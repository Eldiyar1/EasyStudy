from rest_framework import serializers
from googletrans import Translator
from .models import *
from rest_framework.serializers import ModelSerializer


class QuoteSerializers(ModelSerializer):
    translation = serializers.SerializerMethodField()

    # def get_translation(self, obj):
    #     translator = Translator()
    #     if obj.text:
    #         translation = translator.translate(obj.text, dest='ru')
    #         return translation.text
    #     else:
    #         return ''

    def get_translation(self, obj):
        translator = Translator()
        translation = translator.translate(obj.text, dest='ru')
        return translation.text

    class Meta:
        model = Quote
        fields = ['text', 'translation']


class IdiomSerializers(ModelSerializer):
    translation = serializers.SerializerMethodField()

    # def get_translation(self, obj):
    #     translator = Translator()
    #     if obj.text:
    #         translation = translator.translate(obj.text, dest='ru')
    #         return translation.text
    #     else:
    #         return ''
    def get_translation(self, obj):
        translator = Translator()
        translation = translator.translate(obj.text, dest='ru')
        return translation.text

    class Meta:
        model = Idiom
        fields = ['text', 'translation']