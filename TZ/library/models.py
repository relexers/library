from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    id_passport = models.PositiveIntegerField()
    phone = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_taken = models.DateField()

    def __str__(self):
        return self.title



# Create your models here.
