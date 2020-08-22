from rest_framework import serializers
from .models import Project, Pledge

# This is 
class StitchrSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    # size_avail_mens = serializers.ChoiceField(['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL'])
    # size_avail_womens = serializers.ChoiceField(['6', '8', '10', '12', '14', '16', '18', '20'])

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectDetailSerializer(StitchrSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

