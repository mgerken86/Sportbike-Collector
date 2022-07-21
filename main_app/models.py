from django.db import models
from django.urls import reverse

# Create your models here.
class Sportbike(models.Model):
        make =  models.CharField(max_length=100, null=True)
        name = models.CharField(max_length=100, null=True)
        displacement = models.CharField(max_length=30, default='600cc')
        skill_lvl = models.CharField(max_length=50, default='advanced' )

        def __str__(self):
            return f"{self.make} {self.model}"

        def get_absolute_url(self):
            return reverse('detail', kwargs={'sportbike_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    sportbike = models.ForeignKey(Sportbike, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for sportbike_id: {self.sportbike_id} @{self.url}"

