
from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def blake(request):
    return render(request, 'core/blake.html')

def fireflyxl(request):
    return render(request, 'core/fireflyxl.html')

def fireflym(request):
    return render(request, 'core/fireflym.html')

def lc30(request):
    return render(request, 'core/lc30.html')

def helios(request):
    return render(request, 'core/helios.html')

def new(request):
    return render(request, 'core/new.html')

def popular(request):
    return render(request, 'core/popular.html')

def allp(request):
    return render(request, 'core/allp.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    form = ContactoForm()
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'core/contact.html', context)