from django.shortcuts import render
from allauth.account.views import LoginView, SignupView, PasswordResetView



class LogIn(LoginView):
    template_name = 'authentication/login.html'



class SignUp(SignupView):
    template_name = 'authentication/register.html'



class Recover(PasswordResetView):
    template_name = 'authentication/recover.html'