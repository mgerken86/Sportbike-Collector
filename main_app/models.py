from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

NAMES = (
    ('P', 'Premium'),
    ('R', 'Race'),
    ('S', 'Standard')
)

# Create your models here.
class Colors(models.Model):
    color1 = models.CharField(max_length=50, default='black') 
    color2 = models.CharField(max_length=50, default='black') 

    # def __str__(self):
    #     return f"{self.color1} and {self.color2}"

class Sportbike(models.Model):
        make =  models.CharField(max_length=100, null=True)
        name = models.CharField(max_length=100, null=True)
        displacement = models.CharField(max_length=30, default='600cc')
        skill_lvl = models.CharField(max_length=50, default='advanced' )
        colors = models.ManyToManyField(Colors)
        user = models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
            return f"{self.make} {self.name}"

        def get_absolute_url(self):
            return reverse('detail', kwargs={'sportbike_id': self.id})


class Trim(models.Model):
    name = models.CharField(
        max_length=1,
        choices=NAMES,
        default=NAMES[2][0]
    )
    price_inc = models.IntegerField(default=0)

    sportbike = models.ForeignKey(Sportbike, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_name_display()} for ${self.price_inc}"



class Photo(models.Model):
    url = models.CharField(max_length=200)
    sportbike = models.ForeignKey(Sportbike, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for sportbike_id: {self.sportbike_id} @{self.url}"

