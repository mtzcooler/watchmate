from rest_framework import serializers
from watchlist_app.models import Movie
import re

def name_regex(value):
    regex = r'^[a-zA-Z0-9\-\:\s]+$'
    if not re.match(regex, value):
        raise serializers.ValidationError("Title must contain only letters, numbers, dashes, colons and spaces.")

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        # exclude = ['active']
    
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("Title and Description must not be the same.")
        return data
    
    def validate_title(self, value):
        name_regex(value)
        return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(validators=[name_regex])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Title and Description must not be the same.")
#         return data
