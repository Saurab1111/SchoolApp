from django.db import models
from Class.models import Classes
from django.contrib.auth.models import User

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=20)
    roll_no=models.IntegerField()
    class_in= models.ForeignKey(Classes,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Notes(models.Model):
    title= models.CharField(max_length=100)
    note= models.TextField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.title