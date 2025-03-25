import pandas as pd

# Define data for exercises and the muscle groups they train
data = {
    "Exercise": [
        "Push-Ups", "Bench Press", "Chest Fly",
        "Pull-Ups/Chin-Ups", "Bent-Over Rows", "Deadlifts",
        "Overhead Press", "Lateral Raises", "Face Pulls",
        "Bicep Curls", "Tricep Dips", "Hammer Curls",
        "Plank", "Russian Twists", "Leg Raises",
        "Hip Thrusts", "Clamshells", "Lunges",
        "Squats", "Leg Press", "Romanian Deadlifts",
        "Calf Raises", "Neck Flexion/Extension with Resistance Bands",
        "Back Extensions", "Wrist Curls", "Reverse Wrist Curls"
    ],
    "Muscle Groups": [
        "Pectoralis Major, Triceps, Deltoids",
        "Pectoralis Major, Triceps, Anterior Deltoids",
        "Pectoralis Major",
        "Latissimus Dorsi, Biceps, Trapezius",
        "Latissimus Dorsi, Rhomboids, Trapezius, Biceps",
        "Erector Spinae, Glutes, Hamstrings",
        "Deltoids (Anterior, Lateral), Triceps",
        "Lateral Deltoids",
        "Posterior Deltoids, Trapezius",
        "Biceps Brachii, Brachialis",
        "Triceps Brachii, Anterior Deltoids",
        "Brachioradialis, Biceps Brachii",
        "Rectus Abdominis, Transverse Abdominis, Serratus Anterior",
        "Obliques (External, Internal), Rectus Abdominis",
        "Rectus Abdominis, Hip Flexors",
        "Gluteus Maximus, Hamstrings",
        "Gluteus Medius, Gluteus Minimus",
        "Gluteus Maximus, Quadriceps, Hamstrings",
        "Quadriceps, Glutes, Hamstrings",
        "Quadriceps, Glutes",
        "Hamstrings, Glutes",
        "Gastrocnemius, Soleus",
        "Sternocleidomastoid, Splenius Capitis",
        "Erector Spinae, Quadratus Lumborum",
        "Flexor Muscles of the Forearm",
        "Extensor Muscles of the Forearm"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save as CSV
file_path = "/home/wijnandb/sites/15-a-day/static//Exercises_and_Muscle_Groups.csv"
df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")
