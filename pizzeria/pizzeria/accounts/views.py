from django.shortcuts import render,HttpResponseRedirect
from .forms import RegistrazioneForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
# Create your views here.
def registrazione(request):
    if request.method=="POST":
        form=RegistrazioneForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password1"]
            User.objects.create_user(username=username,password=password,email=email)
            user=authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect("/")
    else:
        form=RegistrazioneForm()
    context={"form":form}
    return render(request,"accounts/registrazione.html",context)
