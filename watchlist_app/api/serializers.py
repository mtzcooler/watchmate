from rest_framework import serializers
from watchlist_app.models import Media, Platform, Review
import re

def name_regex(value):
    regex = r'^[a-zA-Z0-9\-\:\s]+$'
    if not re.match(regex, value):
        raise serializers.ValidationError("Title must contain only letters, numbers, dashes, colons and spaces.")


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['media']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):
    # len_title = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Media
        fields = '__all__'
        # exclude = ['active']
    
    def get_len_title(self, obj):
        return len(obj.title)
    
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("Title and Description must not be the same.")
        return data
    
    def validate_title(self, value):
        name_regex(value)
        return value


class PlatformSerializer(serializers.ModelSerializer):
    # media = MediaSerializer(many=True, read_only=True)
    media = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                view_name='media-detail')

    class Meta:
        model = Platform
        fields = '__all__'


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
