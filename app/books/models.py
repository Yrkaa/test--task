from django.db import models


# Create your models here.
class Book_Model(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    isbn = models.CharField(max_length=200)

    def __str__(self):
        return self.name
