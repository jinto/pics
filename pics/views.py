import os
from django.conf import settings
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def random_view(request):
    p = Photo.objects.order_by('?').first()
    return redirect('show', id=p.photo_id)
    #return render(request, 'pics/random.html', {'photo':p})

def next_view(request, id):
    #p = Photo.objects.get(pk=int(id)+1)
    return redirect('show', id=int(id)+1)
    #return render(request, 'pics/random.html', {'photo':p})

def show_view(request, id):
    p = Photo.objects.get(pk=id)
    return render(request, 'pics/show.html', {'photo':p})

def scan_view(request):

    files = []
    for folder in settings.PICS_FOLDER:
        for dirname, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                path=os.path.join(dirname, filename)
                if path.find("@eaDir") < 0 and path.find(".DS") < 0:
                    p, created = Photo.objects.get_or_create(path=path)
                    print(path)

    return render(request, 'pics/scan.html', {'files':files})

def main_view(request):
    return render(request, 'pics/main.html')
