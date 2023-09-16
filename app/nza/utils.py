from nltk.corpus import wordnet
from random import choice
from rest_framework.response import Response
from rest_framework import status
from .models import Word, Synonym, Antonym


def get_random_idiom_or_quote(queryset, serializer_class, error_message):
    if queryset:
        item = choice(queryset)
        serializer = serializer_class(item)
        return Response(serializer.data)
    else:
        return Response({"Ошибка": error_message})


def get_synonyms_and_antonyms(word):
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

        if len(synonyms) >= 4 and len(antonyms) >= 4:
            break

    synonyms = synonyms[:4]
    antonyms = antonyms[:4]

    return synonyms, antonyms

def create_synonyms_and_antonyms(request, *args, **kwargs):
    word = request.data.get('word', '')
    synonyms, antonyms = get_synonyms_and_antonyms(word)

    synonym_list = [{'word': word, 'synonym': synonym} for synonym in synonyms]
    antonym_list = [{'word': word, 'antonym': antonym} for antonym in antonyms]

    Synonym.objects.bulk_create([Synonym(**data) for data in synonym_list])
    Antonym.objects.bulk_create([Antonym(**data) for data in antonym_list])

    return synonyms, antonyms


def get_word_translation_and_image_url(serializer):
    instance = serializer.instance
    word_translation, image_url = serializer.get_translation_and_image_url(instance)

    word_data = serializer.data
    word_data['image_url'] = image_url
    word_data['translation'] = word_translation

    return Response(word_data, status=status.HTTP_200_OK)


def perform_word_creation(serializer):
    last_word = Word.objects.last()
    new_id = (last_word.id + 1) if last_word else 1
    serializer.save(id=new_id)
