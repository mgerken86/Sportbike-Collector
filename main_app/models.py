from django.db import models

# Create your models here.
class Sportbike(models.Model):
        make =  models.CharField(max_length=100, null=True)
        name = models.CharField(max_length=100, null=True)
        displacement = models.CharField(max_length=30, default='600cc')
        skill_lvl = models.CharField(max_length=50, default='advanced' )

        def __str__(self):
            return f"{self.make} {self.model}"