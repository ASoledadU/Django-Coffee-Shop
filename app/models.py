from django.db import models

class Coffee(models.Model):
    item = models.TextField()
    price = models.FloatField()

class Transaction(models.Model):
    time = models.DateTimeField()
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    pre_tax = models.FloatField()
    tax = models.FloatField()
    