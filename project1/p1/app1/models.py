from django.db import models

# Create your models here.
class school(models.Model):
    fnames=models.CharField(max_length=30)
    snames=models.CharField(max_length=30)
    classes=models.IntegerField()
    divi=models.CharField(max_length=2)
    imag=models.ImageField(null=True)
