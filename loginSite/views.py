from django.shortcuts import render, HttpResponseRedirect
from loginSite import forms
from django.contrib.auth import login, logout
from django.urls import reverse, reverse_lazy

# Create your views here.


def sign_up(request):
    form = forms.CreateNewUser
    registered = False
    if request.method == 'POST':
        form = forms.CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True

            pass
    return render(request, 'loginSite/signup.html', context={'title': 'Sign up | Instagram', 'form': form})
