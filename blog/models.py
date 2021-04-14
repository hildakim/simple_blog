from django.db import models

# Create your models here.

class Blog(models.Model):
    food_title = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    upload_date = models.DateTimeField()
    recipe = models.TextField()

    def __str__(self):
        return self.food_title 

    def summary(self):
        return self.recipe[:100]