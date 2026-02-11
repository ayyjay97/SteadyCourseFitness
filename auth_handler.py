import json
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

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
    
    hashed_password = generate_password_hash(password)
    
    users[email] = {
        "password": hashed_password,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "goal_weight": 0,
        "current_weight": 0,
        "plan": [],
        "weight_history": [],
        "run_log": [],
        "selected_plan": None
    }
    _save_users(users)
    return True

def authenticate_user(username, password):
    users = _load_users()
    if username in users:
        stored_hash = users[username]["password"]
        if check_password_hash(stored_hash, password):
            return True
    return False

def get_user_data(username):
    users = _load_users()
    return users.get(username, {})

def update_user_stats(username, goal_weight, current_weight, height=None):
    users = _load_users()
    if username in users:
        users[username]["goal_weight"] = goal_weight
        users[username]["current_weight"] = current_weight
        
        # Only save height if it was passed (Goal Setup), otherwise ignore (Daily Update)
        if height is not None:
            users[username]["height"] = height
        
        # History Logic
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "weight": current_weight
        }
        
        if "weight_history" not in users[username]:
             users[username]["weight_history"] = []
             
        users[username]["weight_history"].append(entry)
        
        _save_users(users)

def add_exercise_to_plan(username, exercise_id):
    users = _load_users()
    if username in users:
        if exercise_id not in users[username]["plan"]:
            users[username]["plan"].append(exercise_id)
            _save_users(users)

def log_run(username, distance, time_str, date):
    users = _load_users()
    if username in users:
        # Calculate pace (min/mile)
        try:
            # Assumes time_str is "MM:SS" or "MM"
            parts = list(map(int, time_str.split(':')))
            total_minutes = parts[0] + (parts[1]/60 if len(parts) > 1 else 0)
            pace_val = total_minutes / float(distance)
            pace_min = int(pace_val)
            pace_sec = int((pace_val - pace_min) * 60)
            pace_display = f"{pace_min}:{pace_sec:02d}/mi"
        except:
            pace_display = "N/A"

        entry = {
            "date": date,
            "distance": distance,
            "time": time_str,
            "pace": pace_display
        }
        
        if "run_log" not in users[username]:
            users[username]["run_log"] = []
            
        users[username]["run_log"].append(entry)
        _save_users(users)

def set_user_goal_plan(username, plan_type):
    users = _load_users()
    if username in users:
        users[username]["selected_plan"] = plan_type
        _save_users(users)