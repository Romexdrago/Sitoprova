from django.urls import path
from .views import pizze_view
urlpatterns = [
    path("pizze/",pizze_view,name="pizze_view")
]
