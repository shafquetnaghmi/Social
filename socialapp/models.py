from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True,null=True)
    photo=models.ImageField(default='default.jpg',upload_to='profile_pic')
    followers=models.ManyToManyField(User,related_name='followers',blank=True)
    following=models.ManyToManyField(User,related_name='following',blank=True)
    def __str__(self): 
        return f'{self.user.username},{self.photo}'

class Image(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='images_created')
    image=models.ImageField(upload_to='images/%d/%m/%y/')
    description=models.TextField(blank=True)
    created=models.DateField(auto_now_add=True,db_index=True)
    users_like=models.ManyToManyField(User,related_name='images_like',blank=True)
    def __str__(self):
        return f'{self.image},{self.description}'

