def get_plan(goal_type):
    plans = {
        "fat_loss": {
            "title": "12-Week Fat Burn",
            "description": "A high-intensity blend of circuit training and cardio designed to maximize calorie burn and improve metabolic conditioning.",
            "weeks": [
                {"week": 1, "focus": "Conditioning Base", "details": "3x Full Body Circuit (Bodyweight), 2x 20min Steady Cardio"},
                {"week": 2, "focus": "Conditioning Base", "details": "3x Full Body Circuit (Light Weight), 2x 25min Steady Cardio"},
                {"week": 3, "focus": "Endurance Build", "details": "3x Full Body Circuit (Reduce Rest to 45s), 3x 20min Steady Cardio"},
                {"week": 4, "focus": "Endurance Build", "details": "3x Full Body Circuit (Add 1 Round), 2x 30min Steady Cardio"},
                {"week": 5, "focus": "Intensity Ramp", "details": "3x Strength Circuits (Moderate Weight), 2x 15min HIIT Sessions"},
                {"week": 6, "focus": "Intensity Ramp", "details": "4x Strength Circuits, 2x 20min HIIT Sessions"},
                {"week": 7, "focus": "Peak Volume", "details": "4x Strength Circuits (Super-sets), 3x 20min Steady Cardio"},
                {"week": 8, "focus": "Peak Volume", "details": "4x Strength Circuits (Reduce Rest to 30s), 3x 25min Steady Cardio"},
                {"week": 9, "focus": "Metabolic Shock", "details": "3x Heavy Circuit, 2x 25min HIIT Sessions"},
                {"week": 10, "focus": "Metabolic Shock", "details": "3x Heavy Circuit, 3x 20min HIIT Sessions"},
                {"week": 11, "focus": "Final Push", "details": "4x Full Body High-Rep Circuit, 2x 45min Long Cardio"},
                {"week": 12, "focus": "Completion", "details": "3x Favorite Circuit (Max Effort), 1x 5k Run Test"}
            ]
        },
        "build_muscle": {
            "title": "Hypertrophy Master",
            "description": "Focuses on volume, time-under-tension, and compound movements to stimulate muscle growth.",
            "weeks": [
                {"week": 1, "focus": "Foundation", "details": "3x Full Body (3 sets of 10 reps), Focus on Form"},
                {"week": 2, "focus": "Foundation", "details": "3x Full Body (3 sets of 12 reps), Slow Eccentrics"},
                {"week": 3, "focus": "Volume Increase", "details": "4x Upper/Lower Split (3 sets of 10 reps)"},
                {"week": 4, "focus": "Volume Increase", "details": "4x Upper/Lower Split (4 sets of 10 reps)"},
                {"week": 5, "focus": "Strength Phase", "details": "4x Push/Pull Split (5 sets of 5 reps, Heavier Weight)"},
                {"week": 6, "focus": "Strength Phase", "details": "4x Push/Pull Split (Increase Weight by 5%)"},
                {"week": 7, "focus": "Hypertrophy Peak", "details": "5x Body Part Split (Chest, Back, Legs, Shoulders, Arms)"},
                {"week": 8, "focus": "Hypertrophy Peak", "details": "5x Body Part Split (Add Drop-sets on final set)"},
                {"week": 9, "focus": "Intensity Techniques", "details": "4x Upper/Lower (Super-sets: Agonist/Antagonist)"},
                {"week": 10, "focus": "Intensity Techniques", "details": "4x Upper/Lower (Rest-Pause Sets)"},
                {"week": 11, "focus": "Max Effort", "details": "3x Full Body Compound (Squat, Bench, Deadlift focus)"},
                {"week": 12, "focus": "Deload & Test", "details": "3x Full Body (Light Weight), Test 1-Rep Maxes on Friday"}
            ]
        },
        "run_time": {
            "title": "Speed & Endurance",
            "description": "Designed to increase your aerobic base and lactate threshold for a faster 5k or 10k time.",
            "weeks": [
                {"week": 1, "focus": "Base Building", "details": "3x 2mi Easy Run, 1x 3mi Long Run"},
                {"week": 2, "focus": "Base Building", "details": "3x 2.5mi Easy Run, 1x 4mi Long Run"},
                {"week": 3, "focus": "Aerobic Capacity", "details": "3x 3mi Easy Run, 1x 5mi Long Run"},
                {"week": 4, "focus": "Aerobic Capacity", "details": "2x 3mi Easy Run, 1x Fartlek Run (Speed Play), 1x 5mi Long Run"},
                {"week": 5, "focus": "Speed Intro", "details": "2x 3mi Easy, 1x Interval Session (4x400m fast), 1x 6mi Long Run"},
                {"week": 6, "focus": "Speed Intro", "details": "2x 3.5mi Easy, 1x Interval Session (6x400m fast), 1x 6mi Long Run"},
                {"week": 7, "focus": "Threshold Work", "details": "2x 4mi Easy, 1x Tempo Run (20min at race pace), 1x 7mi Long Run"},
                {"week": 8, "focus": "Threshold Work", "details": "2x 4mi Easy, 1x Hill Repeats (8x Hill Sprints), 1x 8mi Long Run"},
                {"week": 9, "focus": "Race Specific", "details": "1x 3mi Easy, 1x Interval (3x1mi at race pace), 1x 8mi Long Run"},
                {"week": 10, "focus": "Race Specific", "details": "1x 3mi Easy, 1x Tempo Run (30min hard), 1x 6mi Long Run"},
                {"week": 11, "focus": "Taper", "details": "2x 3mi Easy Run, 1x 2mi at Race Pace (Reduce Volume)"},
                {"week": 12, "focus": "Race Week", "details": "1x 20min Shakeout Run, 1x Time Trial / Race Day (5k or 10k)"}
            ]
        }
    }
    return plans.get(goal_type)