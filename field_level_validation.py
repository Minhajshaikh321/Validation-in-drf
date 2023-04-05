""""
You can specify custom field-level validation by adding .validate_<field_name> methods to your Serializer
subclass.These methods take a single argument, which is the field value that requires validation.
Your validate_<field_name> methods should return the validated value or raise a serializers.ValidationError.
"""

from rest_framework import serializers

class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_title(self,value):
        """
        Check the blog post is about Django
        """
        if 'rest' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Rest")
        return value
