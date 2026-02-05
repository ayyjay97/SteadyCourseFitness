from flask import Flask, render_template, request, redirect, url_for, session
import auth_handler
import data

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
        # Capture both weights
        goal_weight = request.form['goal_weight']
        current_weight = request.form['current_weight']
        
        auth_handler.update_user_stats(session['username'], goal_weight, current_weight)
        return redirect(url_for('dashboard'))
        
    return render_template('goal_setup.html', username=session['username'])

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user_data = auth_handler.get_user_data(session['username'])
    
    # Create the full name string
    full_name = f"{user_data.get('first_name', '')} {user_data.get('last_name', '')}"
    
    # Calculate stats logic
    current = int(user_data.get('current_weight') or 0)
    goal = int(user_data.get('goal_weight') or 0)
    lbs_to_go = current - goal

    # Search logic
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
                           current_weight=current)

@app.route('/update_weight', methods=['GET', 'POST'])
def update_weight():
    if 'username' not in session:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        new_weight = request.form['current_weight']
        user_data = auth_handler.get_user_data(session['username'])
        auth_handler.update_user_stats(session['username'], user_data['goal_weight'], new_weight)
        return redirect(url_for('dashboard'))
        
    return render_template('update_weight.html')

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

@app.route('/credits')
def credits():
    return render_template('credits.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)