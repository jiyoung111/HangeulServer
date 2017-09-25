from rest_framework import serializers
from .models import Word_tbl, Writing_tbl

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word_tbl
        fields = ('wid', 'word', 'wordDesc')

class WritingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Writing_tbl
        fields = ('rid', 'uid', 'wid', 'date', 'writing')