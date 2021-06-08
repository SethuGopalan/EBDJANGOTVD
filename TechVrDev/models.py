from django.db import models

class TechVrDev(models.Model):
    title = models.CharField(max_length=240)
    description =models.TextField()
    technology = models.CharField(max_length=100)
    image= models.FilePathField(path="/img")


