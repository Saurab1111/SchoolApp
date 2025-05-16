from django.db import models

class Schools(models.Model):
    My_choices=[
        ('primary','Primary School'),
        ('secondary','Secondary School')]
    founded_by=models.CharField(max_length=100)
    founded_in=models.DateField()                      #yyyy-mm-dd format
    name= models.CharField(max_length=200)
    type=models.CharField(max_length=20,choices=My_choices)

    def __str__(self):
        return self.name

class Classes(models.Model):
    choices=[
        ('a',"A"),
        ('b',"B"),
        ('c',"C"),
        ('d','D'),
    ]
    std= models.IntegerField()
    div=models.CharField(max_length=2,choices=choices)
    school=models.ForeignKey(Schools,on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.std} {self.div}")

    
