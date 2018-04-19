from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'title' : "Open Bacteria",
        'frase' : "your petri dish",
        'frase2' : "experiment with your petri dish here"
    }
    return render(request,'index.html',context)
