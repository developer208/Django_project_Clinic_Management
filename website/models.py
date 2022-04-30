import email
from unicodedata import name
from django.db import connection, models
from numpy import number
 
class adminDetails(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email=models.CharField(max_length=100)

class patientDetails(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)

class patientClone(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)


def truncate(cls):
    with connection.cursor() as cursor:
        cursor.execute('TRUNCATE TABLE {} CASCADE'.format(cls._meta.db_table))

