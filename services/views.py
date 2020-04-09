from django.shortcuts import render
from .models import Services

# Create your views here.
def index(request):
    return render(request, 'services/index.html')

def about(request):
    return render(request, 'services/about.html')

def specialists(request):
    return render(request, 'services/specialists.html')

def gallery(request):
    return render(request, 'services/gallery.html')

def contact(request):
    return render(request, 'services/contact.html')

def prices(request):
    obj = Services.objects.all()
    context = {
        'object': obj
    }
    return render(request, 'services/prices.html', context)