from distutils import extension
from distutils.command.upload import upload
from email.policy import default
import os
from unicodedata import decimal
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.


class Car( models.Model ):
    name = models.CharField(max_length=255)
    description=models.TextField(default='')
    slug = models.SlugField()
    price = models.DecimalField( max_digits = 10, decimal_places = 2,default=0,blank=True)
    images =models.TextField(blank=True)
    discount=models.IntegerField(default=0)
    # characteristic= models.TextField(default='',blank=True)
    car_type =models.CharField(max_length=255,default='')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class CarSpecs(models.Model):
    gasoline =models.CharField(max_length=255,default='')
    steering =models.CharField(max_length=255,default='')
    capacity =models.CharField(max_length=255,default='')
    car_id=models.IntegerField()
    
class WishList(models.Model):
    user_id =models.IntegerField()
    car_id =models.IntegerField()
    like =models.BooleanField(default=False)

class Review(models.Model):
    rating =models.FloatField(default=0)
    car_id =models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    user_id =models.IntegerField()
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
class Messages(models.Model):
    review_id =models.IntegerField()
    content =models.TextField(default='')
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
  

class Image(models.Model):
    file_name =models.CharField(max_length=255)
    extension_file =models.CharField(max_length=10)
    path =models.ImageField(upload_to=f'%Y{os.sep}%m{os.sep}%d{os.sep}uploads{os.sep}',default=f'%Y{os.sep}%m{os.sep}%d{os.sep}uploads{os.sep}example.jpg')
    
    def extension(self,path):
        name, extension = os.path.splitext(path)
        return extension[1:]
    
    def name(self):
        name = self.path.split("/")[4]
        return name
    
    def save(self, *args, **kwargs):
        self.extension_file = self.extension(self.path)
        self.file_name = self.name()
        super().save(*args, **kwargs)
    
class UserManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError('User must have an email')
        if not username:
            raise ValueError('User must have an username')
        user =self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,password):
        user =self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
        
    
class User(AbstractBaseUser):
    avatar =models.ImageField(upload_to=f'%Y{os.sep}%m{os.sep}%d{os.sep}user{os.sep}',default=f'%Y{os.sep}%m{os.sep}%d{os.sep}user{os.sep}example.jpg')
    biograph=models.TextField(default='')
    email =models.EmailField(verbose_name='Email', max_length=60,unique=True)
    username = models.CharField(max_length=50,unique=True)
    date_joined =models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    is_admin =models.BooleanField(default=False)
    is_staff =models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['username']
    
    objects =UserManager()
    
    def __str__(self):
        return f'{self.username} {self.email}'
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    
    
    