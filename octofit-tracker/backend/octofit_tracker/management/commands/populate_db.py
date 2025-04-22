from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        alice = User.objects.create(username='alice', email='alice@octofit.edu', password='password1')
        bob = User.objects.create(username='bob', email='bob@octofit.edu', password='password2')
        charlie = User.objects.create(username='charlie', email='charlie@octofit.edu', password='password3')

        # Teams
        team_alpha = Team.objects.create(name='Alpha')
        team_beta = Team.objects.create(name='Beta')
        team_alpha.members.add(alice, bob)
        team_beta.members.add(charlie)

        # Workouts
        workout1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        workout2 = Workout.objects.create(name='Strength Builder', description='Full body strength training')

        # Activities
        Activity.objects.create(user=alice, activity_type='Running', duration=timedelta(minutes=30))
        Activity.objects.create(user=bob, activity_type='Cycling', duration=timedelta(minutes=45))
        Activity.objects.create(user=charlie, activity_type='Swimming', duration=timedelta(minutes=25))

        # Leaderboard
        Leaderboard.objects.create(user=alice, score=120)
        Leaderboard.objects.create(user=bob, score=100)
        Leaderboard.objects.create(user=charlie, score=80)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
