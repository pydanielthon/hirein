from django.urls import path
from .views import LogIn, SignUp, Recover



app_name = 'authentication'



urlpatterns = [
    path('login/', LogIn.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('recover/', Recover.as_view(), name='recover'),
]