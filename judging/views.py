from django.views.generic import CreateView
from .models import Team
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import TeamForm

def register(request):


    #really basic, will add more later
    form = TeamForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'form.html', {'form' : form})
