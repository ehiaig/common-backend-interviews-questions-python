from rest_framework import serializers


class RewardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    points = serializers.IntegerField()
    max_per_user = serializers.IntegerField()

class RecommendationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    rewards = RewardSerializer(many=True)