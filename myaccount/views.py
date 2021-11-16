from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from .forms import creeUtilisateur
from django.utils import timezone
from django.contrib import messages
# Create your views here.


def inscription(request):
    form=creeUtilisateur()
    if request.method=='POST':
        form = creeUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, "Compte créé avec succés")
            return redirect('acceslogin')
    context = {'form':form}
    return render(request, 'inscription.html', context)


def acceslogin1(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, "Utilisateur ou mot de passe incorrecte")

    context = {}
    return render(request, 'acceslogin3.html', context)

def acceslogin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Vous etes connecté  {username}.")
				return redirect("home")
			else:
				messages.error(request,"Accès interdit.")
		else:
			messages.error(request,"Utilisateur ou mot de passe incorrecte.")
	form = AuthenticationForm()
	return render(request, 'acceslogin.html', context={'form':form})

def deconnexion(request):
    logout(request)
    return redirect('acceslogin')