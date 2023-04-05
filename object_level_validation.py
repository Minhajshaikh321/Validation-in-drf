"""
To do any other validation that requires access to multiple fields, add a method called .validate() to your 
Serializer subclass. This method takes a single argument, which is a dictionary of field values. It should 
raise a serializers.ValidationError if necessary, or just return the validated values.
"""

from rest_framework import serializers

class EventSerializer(serializers.Serializer):
    description=serializers.CharField(max_length=100)
    start=serializers.IntegerField()
    finish=serializers.IntegerField()

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data
