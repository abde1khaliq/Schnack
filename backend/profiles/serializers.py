from rest_framework import serializers
from .models import DiscordProfile


class DiscordProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordProfile
        fields = ['discord_user_id', 'discord_username', 'mother_language', 'german_level', 'target_level',
                  'correction_style', 'onboarding_complete', 'created_at', 'last_active_at']

class GeminiResponseRequirementSerializer(serializers.Serializer):
        discord_user_id = serializers.IntegerField()
        user_input = serializers.CharField()