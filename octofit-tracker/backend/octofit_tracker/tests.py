from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

# Define tests for users, teams, activity, leaderboard, and workouts
class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        self.assertEqual(user.email, "test@example.com")

class TeamTestCase(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityTestCase(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        activity = Activity.objects.create(activity_id="A1", user=user, type="Running", duration=30)
        self.assertEqual(activity.type, "Running")

class LeaderboardTestCase(TestCase):
    def test_leaderboard_creation(self):
        team = Team.objects.create(name="Test Team")
        leaderboard = Leaderboard.objects.create(leaderboard_id="L1", team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutTestCase(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(workout_id="W1", name="Test Workout", description="Test Description")
        self.assertEqual(workout.name, "Test Workout")
