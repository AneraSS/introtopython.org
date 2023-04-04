def display_statement():
    for exercise, repetition in weight_lifting_exercise.items():
        print(f"- I did {repetition} {exercise}s!")


weight_lifting_exercise = {
    "push-up": 20,
    "squat": 30,
    "deadlift": 15,
    "pull-up": 35,
    "chest-press": 45
}

print("Original dictionary:")
display_statement()

print("\nOne value was altered:")
weight_lifting_exercise["squat"] = 45
display_statement()

print("\n One key-value was added:")
weight_lifting_exercise["dip"] = 15
display_statement()

print("\nRemove one key-value pair:")
del weight_lifting_exercise["squat"]
display_statement()
