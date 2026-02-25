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
            {'username': 'tony_stark', 'first_name': 'Tony', 'last_name': 'Stark', 'email': 'ironman@marvel.com', 'password': 'iamironman'},
            {'username': 'steve_rogers', 'first_name': 'Steve', 'last_name': 'Rogers', 'email': 'cap@marvel.com', 'password': 'avengers1'},
            {'username': 'peter_parker', 'first_name': 'Peter', 'last_name': 'Parker', 'email': 'spidey@marvel.com', 'password': 'webslinger'},
            {'username': 'bruce_banner', 'first_name': 'Bruce', 'last_name': 'Banner', 'email': 'hulk@marvel.com', 'password': 'smash123'},
            {'username': 'natasha_romanoff', 'first_name': 'Natasha', 'last_name': 'Romanoff', 'email': 'blackwidow@marvel.com', 'password': 'widow99'},
            {'username': 'bruce_wayne', 'first_name': 'Bruce', 'last_name': 'Wayne', 'email': 'batman@dc.com', 'password': 'darknight'},
            {'username': 'clark_kent', 'first_name': 'Clark', 'last_name': 'Kent', 'email': 'superman@dc.com', 'password': 'krypton1'},
            {'username': 'diana_prince', 'first_name': 'Diana', 'last_name': 'Prince', 'email': 'wonderwoman@dc.com', 'password': 'themyscira'},
            {'username': 'barry_allen', 'first_name': 'Barry', 'last_name': 'Allen', 'email': 'flash@dc.com', 'password': 'speedforce'},
            {'username': 'hal_jordan', 'first_name': 'Hal', 'last_name': 'Jordan', 'email': 'greenlantern@dc.com', 'password': 'willpower'},
        ]
        users = {}
        for data in users_data:
            user = User.objects.create(**data)
            users[data['username']] = user
            self.stdout.write(f"  Created user: {data['username']}")

        # Create teams
        self.stdout.write('Creating teams...')
        marvel_members = ['tony_stark', 'steve_rogers', 'peter_parker', 'bruce_banner', 'natasha_romanoff']
        dc_members = ['bruce_wayne', 'clark_kent', 'diana_prince', 'barry_allen', 'hal_jordan']

        team_marvel = Team.objects.create(name='Team Marvel', members=marvel_members)
        team_dc = Team.objects.create(name='Team DC', members=dc_members)
        self.stdout.write(f"  Created team: {team_marvel.name}")
        self.stdout.write(f"  Created team: {team_dc.name}")

        # Create activities
        self.stdout.write('Creating activities...')
        activities_data = [
            {'user': 'tony_stark', 'activity_type': 'Iron Man Flight Training', 'duration': 45.0, 'date': datetime.date(2025, 1, 15)},
            {'user': 'steve_rogers', 'activity_type': 'Shield Throwing', 'duration': 60.0, 'date': datetime.date(2025, 1, 15)},
            {'user': 'peter_parker', 'activity_type': 'Web Swinging', 'duration': 30.0, 'date': datetime.date(2025, 1, 16)},
            {'user': 'bruce_banner', 'activity_type': 'Anger Management Run', 'duration': 90.0, 'date': datetime.date(2025, 1, 16)},
            {'user': 'natasha_romanoff', 'activity_type': 'Martial Arts Training', 'duration': 75.0, 'date': datetime.date(2025, 1, 17)},
            {'user': 'bruce_wayne', 'activity_type': 'Night Patrol Parkour', 'duration': 120.0, 'date': datetime.date(2025, 1, 15)},
            {'user': 'clark_kent', 'activity_type': 'Super Speed Running', 'duration': 20.0, 'date': datetime.date(2025, 1, 15)},
            {'user': 'diana_prince', 'activity_type': 'Lasso Combat Training', 'duration': 55.0, 'date': datetime.date(2025, 1, 16)},
            {'user': 'barry_allen', 'activity_type': 'Speed Force Sprint', 'duration': 10.0, 'date': datetime.date(2025, 1, 17)},
            {'user': 'hal_jordan', 'activity_type': 'Green Lantern Construct Building', 'duration': 40.0, 'date': datetime.date(2025, 1, 17)},
        ]
        for data in activities_data:
            Activity.objects.create(**data)
            self.stdout.write(f"  Created activity: {data['user']} - {data['activity_type']}")

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        leaderboard_data = [
            {'user': 'clark_kent', 'score': 9800},
            {'user': 'barry_allen', 'score': 9500},
            {'user': 'bruce_wayne', 'score': 8900},
            {'user': 'tony_stark', 'score': 8700},
            {'user': 'natasha_romanoff', 'score': 8400},
            {'user': 'diana_prince', 'score': 8200},
            {'user': 'steve_rogers', 'score': 8000},
            {'user': 'peter_parker', 'score': 7600},
            {'user': 'hal_jordan', 'score': 7400},
            {'user': 'bruce_banner', 'score': 7000},
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
