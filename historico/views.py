from django.shortcuts import render
from .models import Historico
from django.http import HttpResponse

import logging

# Create your views here.
def index(request):
    if request.method == 'POST':
        logging.info("FEZ O POST")
        logging.info(request.POST)
        Historico.objects.create(temp=request.POST['temp'], feel=request.POST['feels'], dew=request.POST['dew'],
                                 humidity=request.POST['humidity'])
        return HttpResponse(request)
    else:
        logging.info("Nao fez POST")
        historico = Historico.objects.all()
        return render(request, 'historico/index.html', {'historico': historico, 'erro': erro})
