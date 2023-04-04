def crowd_test(names):
    """Tests if the room is being crowded"""
    if len(names) >= 3:
        print("There is more than three people in the room, it's crowded!")
    else:
        print(f"There's less than three people in the room, it ain't crowded")

names = ["Ruth", "Tom", "Martin", "Matija", "Gloria", "Riu"]

crowd_test(names)
