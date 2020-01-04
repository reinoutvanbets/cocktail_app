from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=30)
    picture = models.ImageField()
    glass = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()

    def __str__(self):
        return self.name
