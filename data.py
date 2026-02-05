exercises_db = [
    {
        "id": 1,
        "name": "Barbell Squat",
        "description": "The barbell back squat is a fundamental compound lift "
        "targeting the quads, glutes, hamstrings, and core. Set a barbell on a "
        "rack at upper-chest height, step under it to rest it on your traps, and "
        "unrack it. Squat down with a neutral spine, driving knees outward and "
        "keeping your chest up until thighs are at least parallel to the floor, "
        "then stand up, focusing on driving from the heels. ",
        "image": "assets/barbell_squat.jpg",
        "category": "Legs"
    },
    {
        "id": 2,
        "name": "Bench Press",
        "description": "The bench press is a fundamental weightlifting exercise "
        "where you lie on a flat bench and press a weight (usually a barbell or "
        "dumbbells) upwards from your chest, primarily targeting the chest, shoulders, "
        "and triceps while engaging core and back muscles for stabilization, making "
        "it a powerful upper-body strength builder. It involves a controlled lowering "
        "phase (eccentric) and a powerful pressing phase (concentric) to lift the "
        "weight back up, focusing on proper form like keeping elbows tucked and "
        "shoulder blades pinched for safety and effectiveness.",
        "image": "assets/benchpress.jpg",
        "category": "Chest"
    },
    {
        "id": 3,
        "name": "Treadmill Run",
        "description": "A treadmill run is a controlled indoor cardiovascular "
        "exercise performed on a motorized belt, allowing for precise adjustments "
        "to speed and incline to improve endurance, speed, or fitness. Proper "
        "form involves an upright posture, engaged core, and relaxed shoulders, "
        "aiming for a natural gait without holding the handles. ",
        "image": "assets/treadmill_run.jpg",
        "category": "Cardio"
    },
    {
        "id": 4,
        "name": "Rowing Machine",
        "description": "A rowing machine workout provides a low-impact, full-body "
        "exercise that engages over 86% of your muscles, combining cardiovascular "
        "fitness with strength training by working your legs, core, back, and arms "
        "in each stroke, building endurance and burning significant calories without "
        "stressing joints. It improves posture, flexibility, and strength, making it "
        "suitable for all fitness levels, from beginners needing shorter sessions "
        "(10-15 mins) to advanced users doing longer, interval-based workouts (30-60 mins).",
        "image": "assets/rowing_machine.jpg",
        "category": "Cardio"
    },
    {
        "id": 5,
        "name": "Stationary Bike",
        "description": "A stationary bike workout is a low-impact, cardiovascular "
        "exercise performed on a stationary bicycle to build stamina, strengthen legs, "
        "and burn calories without straining joints. Using adjustable resistance, it "
        "strengthens quadriceps, hamstrings, and glutes while offering versatile training, "
        "from steady-state cardio to high-intensity interval training (HIIT). ",
        "image": "assets/indoor_cycle.jpg",
        "category": "Cardio"
    },
    {
        "id": 6,
        "name": "Outdoor Run",
        "description": "Outdoor running is a dynamic cardiovascular exercise where "
        "both feet leave the ground during each step, propelling the body forward "
        "across varying, uneven terrain, which increases muscle engagement, "
        "particularly in the core and legs, compared to treadmills. It offers "
        "benefits like increased calorie burn due to wind resistance, improved "
        "mental health, and enhanced adaptability through navigating natural obstacles. ",
        "image": "assets/outdoor_run.jpg",
        "category": "Cardio"
    }
]

def get_all_exercises():
    return exercises_db

def get_exercise_by_id(ex_id):
    return next((item for item in exercises_db if item["id"] == ex_id), None)