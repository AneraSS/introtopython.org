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
for name in mountains.keys():
    print(f"- {name}")

print("\nHere are some of the elevations:")
for elevation in mountains.values():
    print(f"- {elevation} m")

print("\nHere is the full key-value dict:")
for name, elevation in mountains.items():
    print(f"- {name} is {elevation} meters tall.")

