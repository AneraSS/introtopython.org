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

for name, elevation_m in mountains.items():
    elevation_ft = round (elevation_m*3.28)
    mountains[name] = [elevation_m, elevation_ft]

print("\nList of mountains:")
for name in mountains.keys():
    print(f"- {name}")

print("\nList of elevations in meters:")
for elevation in mountains.values():
    print(f"- {elevation[0]} m")


print("\nList of elevations in feet:")
for elevation in mountains.values():
    print(f"- {elevation[1]} ft")

print("\nStatements telling how tall each mountain is:")
for name, elevations in mountains.items():
    print(f"- {name} is {elevations[0]} m tall, or {elevations[1]} ft.")



