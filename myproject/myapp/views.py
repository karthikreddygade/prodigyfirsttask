# myapp/views.py
from django.shortcuts import render
from .models import MyModel

def home(request):
    items = MyModel.objects.all()
    return render(request, 'home.html', {'items': items})
