from django.db import models


# Create a new user profile record


class Join_users(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    age= models.IntegerField()
    location=models.CharField(max_length=200)
    interests=models.TextField()
    schedule=models.TextField()
    frequency=models.TextField()
    types=models.TextField()

    
class contact(models.Model):
    email=models.EmailField()
    mobilenumber=models.IntegerField()
    message=models.TextField()
   



# Create your models here.
# class Join_users(models.Model):
#     name=models.CharField(max_length=100)
    
#     news_desc=HTMLField()
#     news_image=models.FileField(upload_to='news/',max_length=300,null=True,default=None)
#     news_slug=AutoSlugField(populates_form='news_title',unique=True,null=True,default=None)
