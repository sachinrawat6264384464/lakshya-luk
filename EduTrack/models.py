from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
   
    mobile = models.CharField(max_length=15)
    address = models.TextField()
   
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)  # store hashed password
    created_at = models.DateTimeField(default=timezone.now)
  
   

    # Methods for password hashing/checking
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'EduTrack_userregistration'
class AdminUser(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, default="Unknown")  # default add karo
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    
   

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'EduTrack_adminuser'  # ✅ Alag table name
class Visiterdata(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    purpose = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'EduTrack_visiterdata'