from django.http import JsonResponse
from .models import Discord_Profile

def get_mother_languages(request):
    choices = Discord_Profile.MOTHER_LANGUAGES
    return JsonResponse([{"label": label, "value": value} for label, value in choices], safe=False)

def get_correction_styles(request):
    choices = Discord_Profile.CORRECTION_STYLES
    return JsonResponse([{"label": label, "value": value} for label, value in choices], safe=False)

def get_target_levels(request):
    choices = Discord_Profile.TARGET_LEVELS
    return JsonResponse([{"label": label, "value": value} for label, value in choices], safe=False)

def get_german_levels(request):
    choices = Discord_Profile.GERMAN_LEVELS
    return JsonResponse([{"label": label, "value": value} for label, value, _ in choices], safe=False)