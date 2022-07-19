from django.shortcuts import render
from django.http import HttpResponse

class Sportbike:
    def __init__(self, make, model, displacement, )

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')    

def sportbikes_index(request):
    return render(request, 'sportbikes/index.html', {'sportbikes': sportbikes})