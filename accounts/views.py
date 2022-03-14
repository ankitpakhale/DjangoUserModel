# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse

from .forms import CustomUserCreationForm

# def test(request):
#     return HttpResponse("bnfdsdkes")

    
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
