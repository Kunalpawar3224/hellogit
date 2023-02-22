from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_name = models.CharField(max_length=30)
    #TODO: to add mandatory 10 numbers
    contant_number = models.IntegerField()   
    emial_id = models.TextField()

    def __str__(self):
        return self.employee_name

