import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    print(request.GET)
    results = []
    objects = list(City.objects.filter(name__istartswith=request.GET['term'][0]))
    for obj in objects:
        results.append(obj.name)
    return JsonResponse(results, safe=False)
