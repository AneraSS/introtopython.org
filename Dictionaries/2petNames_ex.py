def show_dictionary():
    for name, species in pet_names.items():
        print(f"- {name.title()} is a {species}.")

pet_names = {
    "riu": "dog",
    "kira": "cat",
    "mangry": "iguana",
    "perry": "squirrel"
}

print("Original Dictionary:")
show_dictionary()

# modify value
print("\nModify one value in the dictionary:")

pet_names["riu"] = "dog, breed: whippet"

show_dictionary()

# add new key-value pair
print("\n Add a new key-value pair to the dictionary:")

pet_names["laky"] = "dog, breed: german short-hair pointer"

show_dictionary()

# remove one key-value pair
print("\nRemove one key-value pair from the dictionary:")

del pet_names["mangry"]

show_dictionary()

