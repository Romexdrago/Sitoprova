from django.db.models import query
from django.shortcuts import get_object_or_404, render,HttpResponseRedirect,redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RecensioneModelForm
from .models import RecensioneModel
from pizze.models import Pizze
# Create your views here.
def homepage(request):
    user=request.user
    recensione = RecensioneModelForm
    recensioni=RecensioneModel.objects.all()
    return render(request, "core/homepage.html", context={"user": user, "recensione": recensione, "recensioni": recensioni})
def recensione_view(request):
    if request.method=="POST":
        form = RecensioneModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.cliente=request.user
            form.save()
        return HttpResponseRedirect("/")
    else:
        form = RecensioneModelForm()
    context={"recensione": form }
    return render(request,"core/recensione.html",context)
def visualizza_recensioni(request):
    recensioni=RecensioneModel.objects.all()
    context={"recensioni":recensioni}
    return render(request,"core/recensioni.html",context)
@login_required
def profilo_utente(request):
    utente=request.user
    context = {"utente": utente}
    return render(request,"core/profilo.html",context)


def cerca(request):
    if "q" in request.GET:
        querystring = request.GET.get("q")
        if len(querystring) == 0:
            return redirect("/cerca/")
        utenti=User.objects.filter(username__icontains=querystring)
        pizze = Pizze.objects.filter(nome__icontains=querystring)
        context = {"utenti": utenti, "pizze": pizze}
        return render(request,"core/cerca.html",context)
    else:
        return render(request, "core/cerca.html")
def visualizza_pizza(request,pk):
    pizza=get_object_or_404(Pizze,pk=pk)
    context={"pizza":pizza}
    return render(request,"core/pizza.html",context)




