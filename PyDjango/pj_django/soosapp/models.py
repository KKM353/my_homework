from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=200)
    addr = models.TextField()
    rdate = models.DateTimeField()

class Gesipan(models.Model):
    write = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.TextField()
    content = models.TextField()
    tdate = models.DateTimeField()