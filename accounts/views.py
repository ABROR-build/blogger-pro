from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to your login page or any other desired URL
    else:
        # Handle GET requests (optional)
        return render(request, 'registration/logged_out.html')