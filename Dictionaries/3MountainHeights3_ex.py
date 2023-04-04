mountains = {
    "Mount Everest": 8848,
    "K2": 8612,
    "Gurla Mandhata": 7694,
    "Machapuchare": 6993,
    "Cerro El Plomo": 5434,
    "Mont Blanc": 4810,
    "Zugspitze": 2962,
    "Scafell Pike": 978
}

print("Here's a list of mountains:")
for name in sorted(mountains.keys()):
    print(f"- {name}")

print("\nHere are some of the elevations:")
for elevation in sorted(mountains.values()):
    print(f"- {elevation} m")

print("\nHere is the full key-value dict:")
for name, elevation in sorted(mountains.items()):
    print(f"- {name} is {elevation} meters tall.")

