from django.db import models
from accounts.models import User

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()


class Informations(models.Model):
    activity = models.IntergerField()
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


class Foods(models.Model):
    food = models.CharField(max_length=20)
    calorie = models.FloatField()
    cabohydrate = models.FloatField()
    protein = models.FloatField()
class Foods
    
class Meals(models.Model):
    meal_time = models.CharField(max_length=20)
    amount = models.FloatField()
    user_id = models.ForeignKey(User)
    food_id = models.ForeignKey(Foods)
   