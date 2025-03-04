from django.db import models

class User(models.Model):
    nom=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.nom

class PostUser(models.Model):
    titre=models.CharField(max_length=20)
    content=models.CharField(max_length=50)
    def __str__(self):
        return self.content