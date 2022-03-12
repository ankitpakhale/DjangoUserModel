from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
# Create your views here.

def test(request):
    return HttpResponse("You are in user master")

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'