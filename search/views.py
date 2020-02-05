from django.shortcuts import render
from .forms import NewJobForm


def home(request):
    form = NewJobForm()

    context = {'form': form}
    return render(request, 'search/home.html', context)
