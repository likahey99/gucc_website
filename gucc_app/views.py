from django.shortcuts import redirect, render, get_object_or_404
from .models import Garscube, Store, Pool, Committee, Helmet, Kayak, Paddle, BA, Spraydeck, Ball, Miscellaneous
from django.urls import reverse
from django.db import models
# Create your views here.
def index(request):
    return render(request, 'gucc_app/index.html')

def about(request):
    return render(request, 'gucc_app/about.html')

def events(request):    
    return render(request, 'gucc_app/events.html')

def gallery(request):    
    return render(request, 'gucc_app/gallery.html')   

def main_shed(request):     
    return render(request, 'gucc_app/main-shed.html')

def macpherson_shed(request):
    return render(request, 'gucc_app/macpherson-shed.html')

def profile(request):
    return render(request, 'gucc_app/profile.html')

def login(request):  
    context_dict = {'loop':range(1000)} 
    return render(request, 'gucc_app/login.html', context=context_dict)   

def register(request):
    context_dict = {'loop':range(1000)} 
    return render(request, 'gucc_app/register.html', context=context_dict)

def logout(request):    
    return render(request, 'gucc_app/logout.html')

def koalas(request):    
    return render(request, 'gucc_app/koalas.html')

def basekit(request):    
    return render(request, 'gucc_app/includes/basekit.html')

def kayakkit(request):    
    return render(request, 'gucc_app/includes/kayakkit.html')

def baseinventory(request):
    return render(request, 'gucc_app/baseinventory.html')

def test(request):
    return render(request, 'gucc_app/test.html')  

def committee(request):
    committee = Committee.objects.all()
    return render(request, 'gucc_app/committee.html', {'committee': committee})

def welfare(request):
    return render(request, 'gucc_app/welfare.html')

def pool(request):
    pool = Pool.objects.first()

    store = get_object_or_404(Store, name='Pool')

    otherstores = Store.objects.exclude(name='Pool')

    kittypes = [field.name for field in Pool._meta.get_fields() if isinstance(field, models.ManyToManyField)]

    kitheaders = {
        'helmets': ['Id', 'Size', 'Colour', 'Type'],
        'kayaks': ['Id', 'Type', 'Size', 'Colour', 'Slot'],
        'paddles': ['Id', 'Feather', 'Material', 'Group', 'Size', 'RightHanded'],
        'bas': ['Type', 'MainColour', 'InnerColour', 'Number', 'Size'],
        'spraydecks': ['Id', 'DeckSize', 'WaistSize'],
        'balls': ['Id', 'Size'],
        'miscellaneous': ['Id', 'Description']
    }

    context = {
        'storetype': pool,
        'kittypes': kittypes,
        'kitheaders': {kittype: kitheaders.get(kittype, []) for kittype in kittypes},
        'store': store,
        'otherstores': otherstores
    }

    # Render the template with the context
    return render(request, 'gucc_app/pool.html', context) 

def garscube(request):
    garscube = Garscube.objects.first()

    store = get_object_or_404(Store, name='Garscube')

    otherstores = Store.objects.exclude(name='Garscube')

    kittypes = [field.name for field in Garscube._meta.get_fields() if isinstance(field, models.ManyToManyField)]

    kitheaders = {
        'helmets': ['Id', 'Size', 'Colour', 'Type'],
        'kayaks': ['Id', 'Type', 'Size', 'Colour', 'Slot'],
        'paddles': ['Id', 'Feather', 'Material', 'Group', 'Size', 'RightHanded'],
        'bas': ['Type', 'MainColour', 'InnerColour', 'Number', 'Size'],
        'spraydecks': ['Id', 'DeckSize', 'WaistSize'],
        'wetsuits': ['Id', 'Size'],
        'miscellaneous': ['Id', 'Description']
    }

    context = {
        'storetype': garscube,
        'kittypes': kittypes,
        'kitheaders': {kittype: kitheaders.get(kittype, []) for kittype in kittypes},
        'store': store,
        'otherstores': otherstores
    }

    # Render the template with the context
    return render(request, 'gucc_app/pool.html', context) 

def macpherson(request):
    return render(request, 'gucc_app/macpherson.html')