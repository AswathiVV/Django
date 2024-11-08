from django.db import models

# Create your models here.
class movie(models.Model):
    m_name=models.TextField()
    bg_img=models.FileField()
    fg_img=models.FileField()
    duraton=models.TextField()
    category=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.m_name

class Language(models.Model):
    lang=models.TextField()

class Moviefield(models.Model):
    movie=models.ForeignKey(movie,on_delete=models.CASCADE)  
    lang=models.ForeignKey(Language,on_delete=models.CASCADE)  

class Members(models.Model):
    name=models.TextField()
    img=models.FileField()
    position=models.TextField()
    cast=models.BooleanField(default=False)
    crew=models.BooleanField(default=False)
    movie=models.ForeignKey(movie,on_delete=models.CASCADE)    
