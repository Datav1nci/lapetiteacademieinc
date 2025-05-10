from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("set-language/<str:lang_code>/", views.set_language, name="set_language"),
]

