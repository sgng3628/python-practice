from django.db import models
from accpi

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
    calorie = models.CharField(max_length=3)
    cabohydrate = models.CharField(max_length=3)
    fat = models.CharField(max_length=3)
    
    def __str__(self):
        return f'나이:{self.age} 키 :{self.height} 몸무게: {self.weight} 성별: {self.gender} 활동성:{self.activity}'