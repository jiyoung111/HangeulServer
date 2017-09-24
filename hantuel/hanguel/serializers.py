from rest_framework import serializers
from .models import Word_tbl

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word_tbl
        fields = ('wid', 'word', 'wordDesc')
