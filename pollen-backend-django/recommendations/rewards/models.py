from django.db import models

class Reward(models.Model):
    name = models.CharField(max_length=300)
    points = models.IntegerField()
    max_per_user = models.IntegerField()

class Recommendation(models.Model):
    user_id = models.IntegerField()
    rewards = models.ManyToManyField(Reward)
