from django import forms

from .widgets import AjaxInputWidget
from .models import City


def city_choices():
    results = []
    objects = list(City.objects.all())
    i = 0
    for obj in objects:
        results.append((i, obj.name))
        i += 1
    return results


class SearchTicket(forms.Form):
    # Добавьте здесь поля, описанные в задании
    city_from = forms.CharField(widget=AjaxInputWidget(url='api/city_ajax'), label='Город отправления')
    city_to = forms.ChoiceField(label='Город прибытия', widget=forms.Select, choices=city_choices())
    date = forms.DateField(widget=forms.SelectDateWidget, label='Дата')

    class Meta(object):
        model = City
