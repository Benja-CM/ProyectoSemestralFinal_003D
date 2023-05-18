from django.db import models

# Create your models here.
class X(models.Model):
    codid = models.AutoField(primary_key=True, verbose_name='Codigo ID x')
    nombrex = models.CharField(max_length=20, blank=False, null=False)

class X2(models.Model):
    codx = models.CharField(max_length=28)
    nombrex = models.CharField(max_length=30)
    edadx = models.IntegerField()
    foto = models.ImageField(upload_to="x2")
    x = models.ForeignKey(X, on_delete=models.CASCADE)