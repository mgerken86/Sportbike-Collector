from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Sportbike


class SportbikeCreate(CreateView):
    model = Sportbike
    fields = '__all__'
    success_url = '/sportbikes/'


def home(request):
  return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')    

def sportbikes_index(request):
    sportbikes = Sportbike.objects.all()
    return render(request, 'sportbikes/index.html', {'sportbikes': sportbikes})

def sportbikes_detail(request, bike_id):
    bike = Sportbike.objects.get(id=bike_id)
    return render(request, 'sportbikes/detail.html', {'sportbike': bike})