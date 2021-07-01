from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
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

        errors = Show.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)

            return redirect('/shows/new')

        else:
            Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            date = request.POST['date'],
            desc = request.POST['desc'])

            last_show = Show.objects.last().id

            messages.success(request, 'Show created!')

            return redirect(f'/shows/{last_show}')
    else:
        return HttpResponse('Invalid Method')


def view_show(request, number):
    context = {
        'the_show': Show.objects.get(id=number)
    }
    
    return render(request, 'view_show.html', context)

def edit_show(request, number):
    context = {
        'the_show': Show.objects.get(id=number),
        'networks': ['Amazon Prime',  'Disney Plus', 'Netflix', 'Youtube Originals']
    }
    
    return render(request, 'edit_show.html', context)

def update(request, number):

    if request.method == "POST":

        errors = Show.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)

            return redirect(f'/shows/{number}/edit')

        else:
            s = Show.objects.get(id=number)
            s.title = request.POST['title']
            s.network = request.POST['network']
            s.date = request.POST['date']
            s.desc = request.POST['desc']
            s.save()

            messages.success(request, 'Show updated!')

            return redirect(f'/shows/{number}')
    else:
        return HttpResponse('Invalid Method')



def destroy(request, number):

    messages.success(request, 'Show deleted!')

    s = Show.objects.get(id=number)
    s.delete()

    return redirect('/shows')