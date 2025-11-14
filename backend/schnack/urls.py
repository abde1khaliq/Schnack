from django.urls import path
from .views import get_mother_languages

urlpatterns = [
    path('/get_mother_languages/', get_mother_languages, name='get_mother_languages')
]