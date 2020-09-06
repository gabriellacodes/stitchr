from rest_framework import serializers
from .models import CustomUser, UserProfile
import logging
logger = logging.getLogger(__name__)

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    email = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

class UserProfileSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    email = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=5)
    given_name = serializers.CharField(max_length=50)
    preferred_name = serializers.CharField(max_length=50)
    family_name = serializers.CharField(max_length=50)
    shirt_size = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=255)
    suburb = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)
    postcode = serializers.CharField(max_length=5)
    profile_photo = serializers.ImageField()

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.given_name = validated_data.get('given_name', instance.given_name)
        instance.preferred_name = validated_data.get('preferred_name', instance.preferred_name)
        instance.family_name = validated_data.get('family_name', instance.family_name)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.address = validated_data.get('address', instance.address)
        instance.suburb = validated_data.get('suburb', instance.suburb)
        instance.country = validated_data.get('country', instance.country)
        instance.postcode = validated_data.get('postcode', instance.postcode)
        instance.profile_photo = validated_data.get('profile_photo', instance.profile_photo)
        instance.save()
        return instance
