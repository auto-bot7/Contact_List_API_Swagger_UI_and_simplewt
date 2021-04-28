from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    owner= models.ForeignKey(User,blank=False,on_delete=models.CASCADE,related_name='users')
    country_code= models.CharField(max_length=5)
    email=models.EmailField(unique=True)
    phone_no=models.PositiveIntegerField()
    image= models.URLField(null=True, max_length=1000)
    is_favourite= models.BooleanField(default=False)