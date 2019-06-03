from django.db import models
from django.conf import settings

class Board(models.Model):
    title = models.CharField(max_length=20)
    content= models.TextField()
    calorie = models.IntegerField(null=True)
    carbohydrate = models.IntegerField(null=True)
    protein = models.IntegerField(null=True)
    fat = models.IntegerField(null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
# class Foods(models.Model):
#     food = models.CharField(max_length=20)
#     calorie = models.FloatField()
#     cabohydrate = models.FloatField()
#     protein = models.FloatField()
#     fat = models.FloatField()
    
# class Meals(models.Model):
#     meal_time = models.CharField(max_length=20)
#     amount = models.FloatField()
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     food_id = models.ForeignKey(Foods, on_delete=models.CASCADE)
   