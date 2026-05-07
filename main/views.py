from django.shortcuts import render, get_object_or_404
from .models import Berita

def home(request):
    latest_news = Berita.objects.all()[:3]
    return render(request, 'main/home.html', {'latest_news': latest_news})

def profile(request):
    return render(request, 'main/profile.html')

def ppdb(request):
    return render(request, 'main/ppdb.html')

def berita_list(request):
    news = Berita.objects.all()
    return render(request, 'main/berita_list.html', {'news': news})

def berita_detail(request, pk):
    berita_item = get_object_or_404(Berita, pk=pk)
    return render(request, 'main/berita_detail.html', {'berita_item': berita_item})
