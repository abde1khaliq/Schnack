from django.urls import path
from .views import (
    get_mother_languages,
    get_correction_styles,
    get_target_levels,
    get_german_levels,
    DiscordProfileViewset,
    GeminiResponseViewSet,
    UserHistoryViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user_preferences', DiscordProfileViewset, basename='send_user_preference')
router.register(r'gemini', GeminiResponseViewSet, basename='gemini')
router.register(r'user_history', UserHistoryViewSet, basename='user_history')

urlpatterns = [
    path('get_mother_languages/', get_mother_languages, name='get_mother_languages'),
    path('get_correction_styles/', get_correction_styles, name='get_correction_styles'),
    path('get_target_levels/', get_target_levels, name='get_target_levels'),
    path('get_german_levels/', get_german_levels, name='get_german_levels'),
] + router.urls