from django.shortcuts import render

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
    kitlist = [
        {'Id': 1, 'Type': 'Play', 'Size': 'L', 'owner': "Club"},
        {'Id': 2, 'Type': 'Creek', 'Size': 'M', 'owner': "Patrick"},
        {'Id': 3, 'Type': 'Half Slice', 'Size': 'S/M', 'owner': "Club"},
        {'Id': 4, 'Type': 'D', 'Size': '194', 'owner': "Club"},
        
    ]

    kittypes = [
        "Kayaks",
        "Paddles",
        "Helmets",
        "BAs",
        "Spraydecks",
        "Cags",
        "Wetsuits",
        "Safety Kit",
        "Miscellaneous"

    ]    

    kitheaders = [
        "Id",
        "Type",
        "Size",
        "Owner",
    
    ]
    context = {'kitlist': kitlist, 'kittypes': kittypes, 'kitheaders': kitheaders}
    return render(request, 'gucc_app/includes/baseinventory.html', context)

def test(request):
    return render(request, 'gucc_app/test.html')  