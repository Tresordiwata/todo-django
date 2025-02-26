from django.db import models

class User(models.Model):
    nom=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.nom
