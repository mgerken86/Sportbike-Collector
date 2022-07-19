from django.shortcuts import render
from django.http import HttpResponse

class Sportbike:
    def __init__(self, make, model, displacement, skill_lvl):
        self.make =  make
        self.model = model
        self.displacement = displacement
        self.skill_lvl = skill_lvl

sportbikes = [
    Sportbike('Kawasaki', 'ZX-10R', "1000cc", 'Advanced'),
    Sportbike('Yamaha', 'YZF-R1', "1000cc", 'Advanced'),
    Sportbike('Honda', 'CBR-1000RR', "1000cc", 'Advanced'),
    Sportbike('Triumph', 'Daytona 675', "675cc", 'Intermediate'),
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')    

def sportbikes_index(request):
    return render(request, 'sportbikes/index.html', {'sportbikes': sportbikes})