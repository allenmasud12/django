from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    text = {'name': 'Allen Masud', 'work': 'He is a android app developer'}
    return render(request, 'index.html', text)
    
