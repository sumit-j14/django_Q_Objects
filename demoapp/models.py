from django.db import models

# Create your models here.
class Student(models.Model):
    roll_number = models.IntegerField()
    admission_number = models.IntegerField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
