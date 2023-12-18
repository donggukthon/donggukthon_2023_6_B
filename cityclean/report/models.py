from django.db import models
#from django.contrib.auth.models import User

class trashCans(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    picture = models.ImageField(upload_to='picture/')
    information = models.TextField()
    complaincount = models.IntegerField(default=0)