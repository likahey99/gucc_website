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
    return render(request, 'gucc_app/register.html')

def logout(request):    
    return render(request, 'gucc_app/logout.html')

def koalas(request):    
    return render(request, 'gucc_app/koalas.html')