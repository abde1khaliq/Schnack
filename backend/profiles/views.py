from django.http import JsonResponse
from .models import DiscordProfile

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
    return JsonResponse([{"label": label, "value": value} for label, value, _ in choices], safe=False)