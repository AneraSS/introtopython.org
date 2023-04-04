def remove_one(names):
    names.remove(names[-1])

def is_a_mob(names):
    if len(names) > 5:
        print("A mob's in the room.")
    if (len(names) >= 3) and (len(names) < 5):
        print("The room's crowded.")
    if (len(names) >= 1) and (len(names) < 2):
        print("The room ain't crowded.")
    if len(names) == 0:
        print("Here ain't a living soul.")



names = ["Ruth", "Tom", "Martin", "Matija", "Gloria", "Riu"]

is_a_mob(names)

while len(names) >= 4:
    remove_one(names)
is_a_mob(names)

while len(names) >= 2:
    remove_one(names)
is_a_mob(names)

while len(names) > 0:
    remove_one(names)
is_a_mob(names)
# zasto je ovo upalilo?

