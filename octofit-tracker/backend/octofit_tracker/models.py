from django.db import models

# Define models for users, teams, activity, leaderboard, and workouts
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Activity(models.Model):
    activity_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    leaderboard_id = models.CharField(max_length=100, unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

class Workout(models.Model):
    workout_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
