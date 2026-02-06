exercises_db = [
    {
        "id": 1,
        "name": "Barbell Squat",
        "description": "A fundamental compound lift essential for building overall leg power and mass. This exercise primarily targets the quadriceps, hamstrings, and glutes while engaging the core.",
        "image": "assets/barbell_squat.jpg",
        "category": "Lower-Body"
    },
    {
        "id": 2,
        "name": "Bench Press",
        "description": "A standard strength training exercise performed while lying on a weight bench. It focuses on developing the pectorals, anterior deltoids, and triceps.",
        "image": "assets/benchpress.jpg",
        "category": "Upper-Body"
    },
    {
        "id": 3,
        "name": "Treadmill Run",
        "description": "An indoor cardiovascular workout that allows for precise control over speed and incline. This activity works the calves, quadriceps, and hamstrings while improving heart health.",
        "image": "assets/treadmill_run.jpg",
        "category": "Cardio"
    },
    {
        "id": 4,
        "name": "Rowing Machine",
        "description": "A low-impact endurance exercise that mimics the motion of rowing a boat. It provides a full-body workout by targeting the back, legs, arms, and core simultaneously.",
        "image": "assets/rowing_machine.jpg",
        "category": "Cardio"
    },
    {
        "id": 5,
        "name": "Stationary Bike",
        "description": "A joint-friendly cycling workout that can range from steady-state recovery to high-intensity intervals. This exercise strengthens the quadriceps, hamstrings, and calves with minimal impact on the knees.",
        "image": "assets/indoor_cycle.jpg",
        "category": "Cardio"
    },
    {
        "id": 6,
        "name": "Outdoor Run",
        "description": "A functional cardiovascular session performed on natural terrain or pavement. It engages the quads, hamstrings, glutes, and calves while challenging stabilizing muscles.",
        "image": "assets/outdoor_run.jpg",
        "category": "Cardio"
    },
    {
        "id": 7,
        "name": "HIIT",
        "description": "High-Intensity Interval Training involves alternating short bursts of intense effort with rest periods. This training style engages the full body to maximize calorie burn and metabolic rate.",
        "image": "assets/hiit.jpg",
        "category": "Full-Body"
    },
    {
        "id": 8,
        "name": "Kettlebell Swings",
        "description": "A ballistic exercise that builds explosive power and hip mobility. It primarily works the posterior chain, including the glutes, hamstrings, and lower back.",
        "image": "assets/kettlebell_swing.jpg",
        "category": "Full-Body"
    },
    {
        "id": 9,
        "name": "Shoulder Press",
        "description": "An overhead lifting movement designed to build upper body mass and vertical pushing strength. This exercise isolates the deltoids and triceps while requiring core stability.",
        "image": "assets/shoulder_press.jpg",
        "category": "Upper-Body"
    },
    {
        "id": 10,
        "name": "Dumbbell Curl",
        "description": "An isolation exercise focused on building arm size and definition. It specifically targets the biceps brachii muscles in the upper arm.",
        "image": "assets/dumbbell_curl.jpg",
        "category": "Upper-Body"
    },
    {
        "id": 11,
        "name": "Pull Ups",
        "description": "A challenging bodyweight movement that increases upper body width and functional strength. This exercise works the latissimus dorsi, rhomboids, and biceps.",
        "image": "assets/pull-ups.jpg",
        "category": "Upper-Body"
    },
    {
        "id": 12,
        "name": "Deadlift",
        "description": "A powerful compound lift that involves raising a heavy load from the floor to a standing position. It heavily targets the entire posterior chain, including the back, glutes, and hamstrings.",
        "image": "assets/deadlift.jpg",
        "category": "Full-Body"
    },
    {
        "id": 13,
        "name": "Bodyweight Squats",
        "description": "A foundational movement that builds endurance and mobility without equipment. This exercise strengthens the quadriceps, hamstrings, and glutes using your own body weight.",
        "image": "assets/bodyweight_squat.jpg",
        "category": "Lower-Body"
    }
]

def get_all_exercises():
    return exercises_db

def get_exercise_by_id(ex_id):
    return next((item for item in exercises_db if item["id"] == ex_id), None)