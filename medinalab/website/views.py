from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def research(request):
    return render(request, 'website/research.html')

def our_team(request):
    return render(request, 'website/our_team.html')

def publications(request):
    return render(request, 'website/publications.html')

def awards(request):
    return render(request, 'website/awards.html')

def join_us(request):
    return render(request, 'website/join_us.html')

# Create your views here.
