from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, '../templates/start/index.html')


def choose(request):
    return render(request, '../adminPanel/templates/start/choose.html')
