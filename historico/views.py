from django.shortcuts import render
from .models import Historico
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        Historico.objects.create(temp=request.POST['temp'], feel=request.POST['feels'], dew=request.POST['dew'],
                                 humidity=request.POST['humidity'])
        return HttpResponse(request)
    else
        return render(request, 'historico/index.html', {'historico': historico})