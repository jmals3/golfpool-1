from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prof_pic = models.FilePathField()

class Player(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    world_rank = models.PositiveIntegerField(null=True)
    vegas_odds = models.DecimalField(decimal_places=4, max_digits=14, null=True)

class Tournament(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    course = models.CharField(max_length=64)
    city_state_country = models.CharField(max_length=128)
    players = JSONField()
    scores = JSONField()

class Pool(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    buy_in = models.DecimalField(decimal_places=2, max_digits=12)
    prizes = ArrayField(models.DecimalField(decimal_places=2, max_digits=12))

class PoolEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pool = models.PositiveIntegerField()
    picks = JSONField()
    active = models.BooleanField()

class PoolResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pool_entry = models.ForeignKey(PoolEntry, on_delete=models.CASCADE)
