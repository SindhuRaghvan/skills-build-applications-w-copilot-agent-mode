import pymongo
from datetime import timedelta

client = pymongo.MongoClient('localhost', 27017)
db = client['octofit_db']

# Clear collections
db.users.delete_many({})
db.teams.delete_many({})
db.activities.delete_many({})
db.leaderboard.delete_many({})
db.workouts.delete_many({})

# Users
alice = {'username': 'alice', 'email': 'alice@octofit.edu', 'password': 'password1'}
bob = {'username': 'bob', 'email': 'bob@octofit.edu', 'password': 'password2'}
charlie = {'username': 'charlie', 'email': 'charlie@octofit.edu', 'password': 'password3'}
alice_id = db.users.insert_one(alice).inserted_id
bob_id = db.users.insert_one(bob).inserted_id
charlie_id = db.users.insert_one(charlie).inserted_id

# Teams
team_alpha = {'name': 'Alpha', 'members': [alice_id, bob_id]}
team_beta = {'name': 'Beta', 'members': [charlie_id]}
db.teams.insert_one(team_alpha)
db.teams.insert_one(team_beta)

# Workouts
workout1 = {'name': 'Cardio Blast', 'description': 'High intensity cardio workout'}
workout2 = {'name': 'Strength Builder', 'description': 'Full body strength training'}
db.workouts.insert_one(workout1)
db.workouts.insert_one(workout2)

# Activities
db.activities.insert_one({'user': alice_id, 'activity_type': 'Running', 'duration': 30})
db.activities.insert_one({'user': bob_id, 'activity_type': 'Cycling', 'duration': 45})
db.activities.insert_one({'user': charlie_id, 'activity_type': 'Swimming', 'duration': 25})

# Leaderboard
db.leaderboard.insert_one({'user': alice_id, 'score': 120})
db.leaderboard.insert_one({'user': bob_id, 'score': 100})
db.leaderboard.insert_one({'user': charlie_id, 'score': 80})

print('Test data populated successfully.')
