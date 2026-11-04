from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=30)
    instructions=models.TextField()
    ingredients=models.TextField()
    mealtype=models.CharField(max_length=30)
    cuisine=models.CharField(max_length=30)
    image=models.ImageField(upload_to='recipe')

# - `recipename` – CharField
# - `instructions` – TextField
# - `ingredients` – TextField
# - `mealtype` – CharField
# - `cuisine` – CharField
# - `image`  ImageField