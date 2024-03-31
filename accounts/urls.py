from django.urls import path, include
from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name='signup'),
    path('accounts/logout/', views.custom_logout, name='logout_u'),
]