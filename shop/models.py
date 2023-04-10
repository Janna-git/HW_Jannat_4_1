from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchases')
    data_purchase = models.DateTimeField(auto_now_add=True)
