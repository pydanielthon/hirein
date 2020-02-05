from django.shortcuts import render



def home(request):
    navbar = 1 #left menu option

    context = {'navbar': navbar}
    return render(request, 'dashboard/home.html', context)
