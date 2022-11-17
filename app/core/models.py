from django.db import models

class Leaf(models.Model):
    data = models.IntegerField()
    left = models.IntegerField(null=True) #id de nodo a la izquierda
    right = models.IntegerField(null=True) #id de nodo a la derecha
