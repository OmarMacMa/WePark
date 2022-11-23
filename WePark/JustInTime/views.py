from django.shortcuts import render


def index(request):
    return render(request, 'JustInTime/index.html')


def Iframe_prueba(request):
    return render(request, 'JustInTime/Iframe_prueba.html')


def datosProyecto(request):
    return render(request, 'JustInTime/datosProyecto.html')


def estadistic(request):
    return render(request, 'JustInTime/estadistic.html')