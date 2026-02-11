from flask import Flask, render_template, request, redirect, url_for, session
import auth_handler
import data
import plans

app = Flask(__name__)
app.secret_key = "change_this_secret_key"

@app.route('/')
def root():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        if auth_handler.authenticate_user(username, password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid Credentials")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        
        if auth_handler.register_user(email, password, first_name, last_name):
            session['username'] = email
            return redirect(url_for('goal_setup'))
        else:
            return render_template('register.html', error="User already exists")
    return render_template('register.html')

@app.route('/goal_setup', methods=['GET', 'POST'])
def goal_setup():
    if 'username' not in session:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        goal_weight = round(float(request.form['goal_weight']), 2)
        current_weight = round(float(request.form['current_weight']), 2)
        height = round(float(request.form['height']), 2)
        
        auth_handler.update_user_stats(session['username'], goal_weight, current_weight, height)
        return redirect(url_for('dashboard'))
        
    return render_template('goal_setup.html', username=session['username'])

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user_data = auth_handler.get_user_data(session['username'])
    
    full_name = f"{user_data.get('first_name', '')} {user_data.get('last_name', '')}"
    
    current = float(user_data.get('current_weight') or 0)
    goal = float(user_data.get('goal_weight') or 0)
    
    lbs_to_go = round(current - goal, 2)

    all_exercises = data.get_all_exercises()
    query = request.args.get('search_query')
    if query:
        exercises_to_show = [ex for ex in all_exercises if query.lower() in ex['name'].lower()]
    else:
        exercises_to_show = all_exercises

    return render_template('dashboard.html', 
                           full_name=full_name,
                           exercises=exercises_to_show,
                           lbs_to_go=lbs_to_go,
                           current_weight=current,
                           goal_weight=goal)

@app.route('/update_weight', methods=['GET', 'POST'])
def update_weight():
    if 'username' not in session:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        new_weight = round(float(request.form['current_weight']), 2)
        
        user_data = auth_handler.get_user_data(session['username'])
        # Pass the existing height and goal
        existing_height = user_data.get('height')
        existing_goal = user_data.get('goal_weight')
        
        auth_handler.update_user_stats(session['username'], existing_goal, new_weight, existing_height)
        return redirect(url_for('dashboard'))
        
    return render_template('update_weight.html')

@app.route('/weight_history')
def weight_history():
    if 'username' not in session:
        return redirect(url_for('login'))
        
    user_data = auth_handler.get_user_data(session['username'])
    # Get the history list, default to empty if missing
    history = user_data.get('weight_history', [])
    
    # Reverse the list so newest dates appear first
    history = list(reversed(history))
    
    return render_template('weight_history.html', history=history)

@app.route('/my_plan')
def my_plan():
    if 'username' not in session:
        return redirect(url_for('login'))
        
    user_data = auth_handler.get_user_data(session['username'])
    plan_ids = user_data.get('plan', [])
    
    # Convert IDs back to full exercise objects
    saved_exercises = [data.get_exercise_by_id(pid) for pid in plan_ids]
    
    return render_template('my_plan.html', plan=saved_exercises)

@app.route('/exercise/<int:exercise_id>')
def exercise_detail(exercise_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    exercise = data.get_exercise_by_id(exercise_id)
    return render_template('exercise_detail.html', exercise=exercise)

@app.route('/add_to_plan/<int:exercise_id>')
def add_to_plan(exercise_id):
    if 'username' not in session:
        return redirect(url_for('login'))
        
    auth_handler.add_exercise_to_plan(session['username'], exercise_id)
    return redirect(url_for('my_plan'))

@app.route('/running_log', methods=['GET', 'POST'])
def running_log():
    if 'username' not in session: return redirect(url_for('login'))
    
    if request.method == 'POST':
        date = request.form['date']
        dist = request.form['distance']
        time = request.form['time']
        auth_handler.log_run(session['username'], dist, time, date)
        return redirect(url_for('running_log'))

    user_data = auth_handler.get_user_data(session['username'])
    logs = user_data.get('run_log', [])
    return render_template('running_log.html', logs=reversed(logs))

@app.route('/pace_calculator', methods=['GET', 'POST'])
def pace_calculator():
    if 'username' not in session: return redirect(url_for('login'))
    
    result = None
    if request.method == 'POST':
        try:
            dist = float(request.form['distance'])
            mins = float(request.form['minutes'])
            pace = mins / dist
            p_min = int(pace)
            p_sec = int((pace - p_min) * 60)
            
            # Projections
            mile_time = pace
            k5_time = pace * 3.1
            k10_time = pace * 6.2
            
            result = {
                "pace": f"{p_min}:{p_sec:02d}",
                "5k": f"{int(k5_time)}:{int((k5_time%1)*60):02d}",
                "10k": f"{int(k10_time)}:{int((k10_time%1)*60):02d}"
            }
        except:
            result = {"error": "Invalid Input"}
            
    return render_template('pace_calculator.html', result=result)

@app.route('/plan_selection')
def plan_selection():
    if 'username' not in session: return redirect(url_for('login'))
    return render_template('goal_selection.html')

@app.route('/set_plan/<plan_type>')
def set_plan(plan_type):
    if 'username' not in session: return redirect(url_for('login'))
    auth_handler.set_user_goal_plan(session['username'], plan_type)
    return redirect(url_for('my_weekly_plan'))

@app.route('/my_weekly_plan')
def my_weekly_plan():
    if 'username' not in session: return redirect(url_for('login'))
    
    user_data = auth_handler.get_user_data(session['username'])
    plan_type = user_data.get('selected_plan')
    
    if not plan_type:
        return redirect(url_for('plan_selection'))
        
    plan_data = plans.get_plan(plan_type)
    return render_template('weekly_plan.html', plan=plan_data)

@app.route('/credits')
def credits():
    return render_template('credits.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)