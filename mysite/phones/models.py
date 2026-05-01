from django.db import models

# Create your models here.

class Phone(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='phones')

    def __str__(self):
        return self.name