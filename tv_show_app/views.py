from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    return redirect('/shows')

def all_shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def new_show(request):
    
    return render(request, 'new_show.html')

def create(request):
    if request.method == "POST":
        Show.objects.create(
        title = request.POST['title'],
        network = request.POST['net'],
        date = request.POST['date'],
        desc = request.POST['desc'])
    return redirect('/shows')

def view_show(request, number):
    context = {
        'the_show': Show.objects.get(id=number)
    }
    
    return render(request, 'view_show.html', context)

def edit_show(request, number):
    context = {
        'the_show': Show.objects.get(id=number)
    }
    
    return render(request, 'edit_show.html', context)

def update(request, number):
    s = Show.objects.get(id=number)
    s.title = request.POST['title']
    s.network = request.POST['net']
    s.date = request.POST['date']
    s.desc = request.POST['desc']
    s.save()

    return redirect(f'/shows/{number}')

def destroy(request, number):
    s = Show.objects.get(id=number)
    s.delete()

    return redirect('/shows')