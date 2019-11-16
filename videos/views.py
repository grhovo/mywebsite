from django.shortcuts import render
from django.http import HttpResponse
from .models import Videos
# Create your views here.

def index(request):
    videos = Videos.objects.order_by()

    return render(request,'videos/list.html' , {'videos':videos})
