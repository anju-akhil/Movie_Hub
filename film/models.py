from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Genre(models.Model):
    type=models.CharField(max_length=200,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.type

class Language(models.Model):
    language=models.CharField(max_length=200,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.language

class Actors(models.Model):
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Movies(models.Model):
    title=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    genres=models.ManyToManyField(Genre)
    language=models.ForeignKey(Language,on_delete=models.CASCADE,null=True)
    director=models.CharField(max_length=200)
    actors=models.ManyToManyField(Actors)
    description=models.TextField(max_length=500)
    poster=models.ImageField(upload_to="posterimg",default="default.jpg")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    is_trending=models.BooleanField(default=False)

    @property 
    def reviews(self):
        return self.review_movie.all()
    
    @property
    def review_count(self):
        qs=self.reviews
        return qs.count

    def __str__(self):
        return self.title  
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile",null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
class Review(models.Model):
    rating=models.PositiveIntegerField()
    comments=models.TextField(max_length=500)
    user=models.ForeignKey(UserProfile,on_delete=models.DO_NOTHING)
    movies=models.ForeignKey(Movies,on_delete=models.DO_NOTHING,related_name="review_movie",null=True)

def create_userprofile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_userprofile,sender=User)
