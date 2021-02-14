from django.db import models

# Create your models here.

class Background(models.Model):
    photo = models.ImageField(default = "default.jpg", upload_to = 'background')
