def remove_one(names):
    """Removes the last name in the list"""
    names.remove(names[-1])

def crowd_test(names):
    """Tests if the room is being crowded"""
    if len(names) >= 3:
        print("There is more than three people in the room, it's crowded!")

# kako napisati program koji briše samo zadnja tri?

names = ["Ruth", "Tom", "Martin", "Matija", "Gloria", "Riu"]

crowd_test(names)

while len(names) > 2:
    remove_one(names)
print(f"Now it's two people: {names}; therefore the room ain't crowded.")