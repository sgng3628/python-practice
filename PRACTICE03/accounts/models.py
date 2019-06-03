from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    ACTIVITY_CHOICES = (
        ('1', '비활동적'),
        ('2', '저활동적'),
        ('3', '활동적'),
        ('4', '매우 활동적'),
    )
    activity = models.CharField(max_length=1, choices= ACTIVITY_CHOICES)
    calorie = models.IntegerField(null=True)
    carbohydrate_low = models.IntegerField(null=True)
    carbohydrate_high = models.IntegerField(null=True)
    protein_low = models.IntegerField(null=True)
    protein_high = models.IntegerField(null=True)
    fat_low = models.IntegerField(null=True)
    fat_high = models.IntegerField(null=True)
    