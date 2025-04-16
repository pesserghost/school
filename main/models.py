from django.db import models

class Class(models.Model):
    cla_ss = models.IntegerField(unique=True)

    def __str__(self):
        return self.cla_ss

class Teacher(models.Model):
    full_name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cla_ss = models.ManyToManyField(Class)

    def __str__(self):
        return self.full_name

class Student(models.Model):
    full_name = models.CharField(max_length=250)
    cla_ss = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name