from random import choice
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response
from .models import *
from .serializers import QuoteSerializers,IdiomSerializers


# Create your views here.

class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializers

    def list(self, request):
        quote = choice(self.queryset)
        serializer = self.serializer_class(quote)
        return Response(serializer.data)


class IdiomViewSet(ModelViewSet):
    queryset = Idiom.objects.all()
    serializer_class = IdiomSerializers

    def list(self, request):
        idiom = choice(self.queryset)
        serializer = self.serializer_class(idiom)
        return Response(serializer.data)

