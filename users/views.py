from django.shortcuts import render
from users.models import Background
import io
from django.http import FileResponse
# from reportlab.pdfgen import canvas
# Create your views here.

def base(request):
    return render(request, 'users/base.html')

def index(request):
    # images = Background.objects.all()
    return render(request, 'users/index.html')

def more(request):
    return render(request, 'users/more.html')

def formations(request):
    return render(request, 'users/formations.html')

