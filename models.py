from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('Date Posted')
    images = models.ImageField(null=True,blank=True, upload_to='image/') #allow us to not have an imagine if we dont want it
