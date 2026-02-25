from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
import datetime


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create users (superheroes)
        self.stdout.write('Creating users...')
        users_data = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'password': 'iamironman'},
            {'name': 'Steve Rogers', 'email': 'cap@marvel.com', 'password': 'avengers1'},
            {'name': 'Peter Parker', 'email': 'spidey@marvel.com', 'password': 'webslinger'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com', 'password': 'smash123'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'password': 'widow99'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'password': 'darknight'},
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'password': 'krypton1'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'password': 'themyscira'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com', 'password': 'speedforce'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com', 'password': 'willpower'},
        ]
        users = {}
        for data in users_data:
            user = User.objects.create(**data)
            users[data['name']] = user
            self.stdout.write(f"  Created user: {data['name']}")

        # Create teams
        self.stdout.write('Creating teams...')
        marvel_members = ['Tony Stark', 'Steve Rogers', 'Peter Parker', 'Bruce Banner', 'Natasha Romanoff']
        dc_members = ['Bruce Wayne', 'Clark Kent', 'Diana Prince', 'Barry Allen', 'Hal Jordan']

        team_marvel = Team.objects.create(name='Team Marvel', members=marvel_members)
        team_dc = Team.objects.create(name='Team DC', members=dc_members)
        self.stdout.write(f"  Created team: {team_marvel.name}")
        self.stdout.write(f"  Created team: {team_dc.name}")

        # Create activities
        self.stdout.write('Creating activities...')
        activities_data = [
            {'user': 'Tony Stark', 'activity_type': 'Iron Man Flight Training', 'duration': 45.0, 'date': datetime.date(2025, 1, 15)},
            {'user': 'Steve Rogers', 'activity_type': 'Shield Throwing', 'duration': 60.0, 'date': datetime.date(2025, 1, 15)},
            {'user': 'Peter Parker', 'activity_type': 'Web Swinging', 'duration': 30.0, 'date': datetime.date(2025, 1, 16)},
            {'user': 'Bruce Banner', 'activity_type': 'Anger Management Run', 'duration': 90.0, 'date': datetime.date(2025, 1, 16)},
            {'user': 'Natasha Romanoff', 'activity_type': 'Martial Arts Training', 'duration': 75.0, 'date': datetime.date(2025, 1, 17)},
            {'user': 'Bruce Wayne', 'activity_type': 'Night Patrol Parkour', 'duration': 120.0, 'date': datetime.date(2025, 1, 15)},
            {'user': 'Clark Kent', 'activity_type': 'Super Speed Running', 'duration': 20.0, 'date': datetime.date(2025, 1, 15)},
            {'user': 'Diana Prince', 'activity_type': 'Lasso Combat Training', 'duration': 55.0, 'date': datetime.date(2025, 1, 16)},
            {'user': 'Barry Allen', 'activity_type': 'Speed Force Sprint', 'duration': 10.0, 'date': datetime.date(2025, 1, 17)},
            {'user': 'Hal Jordan', 'activity_type': 'Green Lantern Construct Building', 'duration': 40.0, 'date': datetime.date(2025, 1, 17)},
        ]
        for data in activities_data:
            Activity.objects.create(**data)
            self.stdout.write(f"  Created activity: {data['user']} - {data['activity_type']}")

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        leaderboard_data = [
            {'user': 'Clark Kent', 'score': 9800},
            {'user': 'Barry Allen', 'score': 9500},
            {'user': 'Bruce Wayne', 'score': 8900},
            {'user': 'Tony Stark', 'score': 8700},
            {'user': 'Natasha Romanoff', 'score': 8400},
            {'user': 'Diana Prince', 'score': 8200},
            {'user': 'Steve Rogers', 'score': 8000},
            {'user': 'Peter Parker', 'score': 7600},
            {'user': 'Hal Jordan', 'score': 7400},
            {'user': 'Bruce Banner', 'score': 7000},
        ]
        for data in leaderboard_data:
            Leaderboard.objects.create(**data)
            self.stdout.write(f"  Created leaderboard entry: {data['user']} - {data['score']}")

        # Create workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'name': 'Iron Man Power Suit Workout',
                'description': 'High-intensity resistance training inspired by Tony Stark\'s Iron Man suit.',
                'exercises': ['Repulsor Pulse Push-ups', 'Arc Reactor Core Hold', 'Flight Simulator Squats', 'JARVIS-guided Plank'],
            },
            {
                'name': 'Captain America Shield Circuit',
                'description': 'Full-body circuit training for super-soldier endurance.',
                'exercises': ['Shield Throw Rotations', 'Brooklyn Brawler Punches', 'Super Soldier Run', 'Vibranium Deadlift'],
            },
            {
                'name': 'Spider-Man Agility Course',
                'description': 'Flexibility and agility training inspired by Peter Parker.',
                'exercises': ['Web Swing Pull-ups', 'Wall Crawl Lunges', 'Spider Sense Dodges', 'Upside-Down Crunches'],
            },
            {
                'name': 'Batman Gotham Gauntlet',
                'description': 'Dark Knight night-training for peak human performance.',
                'exercises': ['Bat-Grapple Pull-ups', 'Gotham Parkour Sprint', 'Batarang Balance Drill', 'Cave Darkness Yoga'],
            },
            {
                'name': 'Wonder Woman Amazonian Training',
                'description': 'Powerful combat and strength training from Themyscira.',
                'exercises': ['Lasso Spin Squats', 'Amazonian Shield Block', 'Olympus Overhead Press', 'Godkiller Sword Lunges'],
            },
        ]
        for data in workouts_data:
            Workout.objects.create(**data)
            self.stdout.write(f"  Created workout: {data['name']}")

        self.stdout.write(self.style.SUCCESS('\nDatabase populated successfully!'))
        self.stdout.write(f"  Users: {User.objects.count()}")
        self.stdout.write(f"  Teams: {Team.objects.count()}")
        self.stdout.write(f"  Activities: {Activity.objects.count()}")
        self.stdout.write(f"  Leaderboard: {Leaderboard.objects.count()}")
        self.stdout.write(f"  Workouts: {Workout.objects.count()}")
