from django.urls import path
from .views import homepage,profilo_utente,recensione_view,cerca,visualizza_pizza
urlpatterns = [
    path("",homepage,name="homepage"),
    path("profilo/",profilo_utente, name="profilo_view"),
    path("recensione/", recensione_view, name="recensione_view"),
    path("cerca/", cerca, name="cerca_view"),
    path("pizza/<int:pk>/", visualizza_pizza, name="visualizza_pizza_view"),
]
