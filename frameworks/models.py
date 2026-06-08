from django.db import models

# Create your models here.

class Student(models.Model):
   
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    course = models.CharField(max_length = 100)
class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 100)
    student = models.ForeignKey(Student,on_delete = models.CASCADE)   

class Subject(models.Model):
    name = models.CharField(max_length= 10)
    subject_teacher_name = models.CharField(max_length = 10)

    def __str__(self):
        return self.name
    