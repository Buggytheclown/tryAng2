from django.shortcuts import render


def AngIndex (request):
    return render (request, 'Angular2/index.html')