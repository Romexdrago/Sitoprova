from django.urls import path
from .views import registrazione
urlpatterns = [
    path("registrazione/",registrazione,name="registrazione_view")
]
