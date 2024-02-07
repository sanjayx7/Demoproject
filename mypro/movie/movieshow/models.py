# Create your models here.
from django.db import models

# Create your models here.
class movieshow(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    year=models.IntegerField()
    image=models.ImageField(upload_to="movieshow/images",null=True,blank=True)
    def __str__(self):
        return f"{self.name} by {self.description}"