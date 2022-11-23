from django.shortcuts import render


def index(request):
    return render(request, 'JustInTime/index.html')

def Iframe(request):
    return render(request, 'JustInTime/Iframe.html')