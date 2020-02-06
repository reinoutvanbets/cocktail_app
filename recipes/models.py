from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=False)
    brand = models.CharField(max_length=100, blank=True, null=True)
    dateCreated = models.DateField("date Created", auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    glass = models.CharField(max_length=50, blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    picture = models.ImageField()
    instructions = models.TextField()
    dateCreated = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
