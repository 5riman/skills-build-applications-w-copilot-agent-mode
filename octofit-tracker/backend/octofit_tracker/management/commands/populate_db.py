from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient()
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "user1@example.com", "name": "User One"},
            {"email": "user2@example.com", "name": "User Two"},
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team Alpha"},
            {"name": "Team Beta"},
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"activity_id": "A1", "user": "user1@example.com", "type": "Running", "duration": 30},
            {"activity_id": "A2", "user": "user2@example.com", "type": "Cycling", "duration": 45},
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"leaderboard_id": "L1", "team": "Team Alpha", "points": 100},
            {"leaderboard_id": "L2", "team": "Team Beta", "points": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"workout_id": "W1", "name": "Workout One", "description": "Description for Workout One"},
            {"workout_id": "W2", "name": "Workout Two", "description": "Description for Workout Two"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
