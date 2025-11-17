from rest_framework.decorators import action
from rest_framework import viewsets, mixins, status, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from .models import DiscordProfile, MessageHistory
from .serializers import (
    DiscordProfileSerializer,
    GeminiResponseRequirementSerializer,
    UserHistorySerializer
)
from .gemini_engine import GeminiEngine


def get_mother_languages(request):
    choices = DiscordProfile.MOTHER_LANGUAGES
    return JsonResponse([{"label": label, "value": value} for label, value in choices], safe=False)


def get_correction_styles(request):
    choices = DiscordProfile.CORRECTION_STYLES
    return JsonResponse([{"label": label, "value": value} for label, value in choices], safe=False)


def get_target_levels(request):
    choices = DiscordProfile.TARGET_LEVELS
    return JsonResponse([{"label": label, "value": value} for label, value in choices], safe=False)


def get_german_levels(request):
    choices = DiscordProfile.GERMAN_LEVELS
    return JsonResponse([{"label": label, "value": value} for label, value in choices], safe=False)


class DiscordProfileViewset(
        mixins.RetrieveModelMixin, mixins.CreateModelMixin,
        mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = DiscordProfileSerializer
    queryset = DiscordProfile.objects.all()


class UserHistoryViewSet(
        mixins.RetrieveModelMixin, mixins.CreateModelMixin,
        mixins.ListModelMixin, mixins.UpdateModelMixin,
        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = UserHistorySerializer
    queryset = MessageHistory.objects.all()


class GeminiResponseViewSet(viewsets.GenericViewSet):
    serializer_class = GeminiResponseRequirementSerializer

    @action(methods=['post'], detail=False, url_path='respond')
    def respond_to_user(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            discord_user_id = serializer.validated_data['discord_user_id']
            user_input = serializer.validated_data['user_input']

            user_message_history = (
                MessageHistory.objects
                .filter(user=discord_user_id)
                .order_by('created_at')[:50]
            )

            history = [
                {
                    "user_message": msg.user_message,
                    "schnack_response": msg.schnack_response
                }
                for msg in user_message_history
            ]

            try:
                user = DiscordProfile.objects.get(
                    discord_user_id=discord_user_id)
            except DiscordProfile.DoesNotExist:
                return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

            engine = GeminiEngine()
            response = engine.get_response(
                discord_user_id=user.discord_user_id,
                username=user.discord_username,
                user_german_level=user.german_level,
                user_mother_language=user.mother_language,
                user_target_level=user.target_level,
                user_correction_style=user.correction_style,
                user_input=user_input,
                user_message_history=history
            )

            return Response({"response": response}, status=status.HTTP_200_OK)

        except Exception as error:
            print("⚠️ An error occurred during response process:", error)
            return Response({"detail": "Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)