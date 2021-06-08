from django.shortcuts import render
from .models import Pizze
from django.contrib.auth.models import User
# Create your views here.
def pizze_view(request):
    pizze=Pizze.objects.all().order_by("nome")
    user=request.user
    context={"pizze":pizze,"user":user}
    return render(request,"pizze.html",context)
