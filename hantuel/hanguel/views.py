from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from hantuel.hanguel.serializers import WordSerializer, WritingSerializer
from .models import Word_tbl, Writing_tbl
from rest_framework import viewsets
import random


class WordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Word_tbl.objects.all()
    serializer_class = WordSerializer

@api_view(['GET', 'POST'])
def writing_list(request):
    """
    List all wiritings, or create a new writing.
    """
    if request.method == 'GET':
        writings = Writing_tbl.objects.all()
        serializer = WritingSerializer(writings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WritingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def word_detail(request):
    """
    Retrieve, update or delete a snippet instance.
    """
    num = random.randint(1,6)
    try:
        word = Word_tbl.objects.get(pk=num)
    except word.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordSerializer(word)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def writing_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Writing_tbl.objects.get(pk=pk)
    except Writing_tbl.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WritingSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WritingSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def view_writing(request, pk):
     try:
        writing = Writing_tbl.objects.get(pk=pk)
     except Writing_tbl.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WritingSerializer(writing)
        return Response(serializer.data)
