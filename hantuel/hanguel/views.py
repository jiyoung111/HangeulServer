from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from hanguel.hanguel.serializers import WordSerializer
from .models import Word_tbl
import random

@api_view(['GET'])
def word_detail(request):
    """
    Retrieve, update or delete a snippet instance.
    """
    num = random.randint(1,791)
    try:
        word = Word_tbl.objects.get(pk=num)
    except word.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordSerializer(word)
        return Response(serializer.data)


