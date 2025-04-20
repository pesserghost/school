from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.CharField(max_length=10, choices=[
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student')
    ])

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='users/teachers', null=True, blank=True)
    experience = models.IntegerField(default=1)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='users/students', null=True, blank=True)

class Class(models.Model):
    cla_ss = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.cla_ss)