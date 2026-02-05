import json
import os

USER_DB = "users.json"

def _load_users():
    if not os.path.exists(USER_DB):
        return {}
    with open(USER_DB, 'r') as f:
        return json.load(f)

def _save_users(users):
    with open(USER_DB, 'w') as f:
        json.dump(users, f, indent=4)

def register_user(email, password, first_name, last_name):
    users = _load_users()
    if email in users:
        return False
    
    users[email] = {
        "password": password,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "goal_weight": 0,
        "current_weight": 0,
        "plan": [] 
    }
    _save_users(users)
    return True

def authenticate_user(username, password):
    users = _load_users()
    if username in users and users[username]["password"] == password:
        return True
    return False

def get_user_data(username):
    users = _load_users()
    return users.get(username, {})

def update_user_stats(username, goal_weight, current_weight):
    users = _load_users()
    if username in users:
        users[username]["goal_weight"] = goal_weight
        users[username]["current_weight"] = current_weight
        _save_users(users)

def add_exercise_to_plan(username, exercise_id):
    users = _load_users()
    if username in users:
        if exercise_id not in users[username]["plan"]:
            users[username]["plan"].append(exercise_id)
            _save_users(users)