def get_mountain_range(name):
    return ranges[name]



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

ranges = {
    "Mount Everest": "Nepal",
    "K2": "Pakistan",
    "Gurla Mandhata": "China",
    "Machapuchare": "Nepal",
    "Cerro El Plomo": "Chile",
    "Mont Blanc": "France",
    "Zugspitze": "Germany",
    "Scafell Pike": "England"
}

for name, elevation in mountains.items():
    mountains[name] = {"elevation": elevation, "range": get_mountain_range(name)}

print("Mountain names:")
for name in mountains.keys():
    print(f"- {name}")

print(f"\nMountain elevations in meters:")
for mt_description in mountains.values():
    print(f"- {mt_description['elevation']}")

print(f"\nMountain ranges:")
for mt_description in mountains.values():
    print(f"- {mt_description['range']}")

print("\nSeries of statements that say everything you know about each mountain: ")
for name, mt_description in mountains.items():
    print(f"- {name} is an {mt_description['elevation']}-meter tall mountain in the {mt_description['range']} range. ")