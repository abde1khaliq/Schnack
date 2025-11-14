from django.http import JsonResponse
from .models import Discord_Profile

def get_mother_languages(request):
    choices = Discord_Profile.MOTHER_LANGUAGES
    return JsonResponse([{"label": label, "value": value} for label, value in choices], safe=False)