"""
Individual fields on a serializer can include validators, by declaring them on the field instance.
"""

from . import GameRecordSerializer
from rest_framework import serializers

def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

class GameRecordSerializer(serializers.Serializer):
    score = IntegerField(validators=[multiple_of_ten])
