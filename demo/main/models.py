from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=120)
    img=CloudinaryField('image')