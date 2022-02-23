from django.db import models

# Create your models here.

class Score(models.Model):
	input_str = models.CharField(max_length=50)
	sum_score = models.IntegerField()