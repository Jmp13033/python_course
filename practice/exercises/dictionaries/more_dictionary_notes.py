"""
===========================================
Python Dictionaries - Next Steps
===========================================

Read dictionary_notes.py first.
These examples combine dictionaries with lists and loops you know.
Run this file to see the results!
"""

# ==================================================
# 1 - Update Several Values
# ==================================================

player = {"name": "Alex", "level": 2, "coins": 50}

# update() changes existing keys and adds new keys.
player.update({"level": 3, "pet": "Wolf"})
print("Updated player:", player)

# ==================================================
# 2 - A List Inside a Dictionary
# ==================================================

player["inventory"] = ["Sword", "Potion"]

# First get the list using its key, then use a list method.
player["inventory"].append("Shield")
print("\nFirst item:", player["inventory"][0])

print("Inventory:")
for item in player["inventory"]:
    print(f"- {item}")

# ==================================================
# 3 - A Dictionary Inside a Dictionary
# ==================================================

# Each player name is a key. Each value is another dictionary.
players = {
    "Alex": {"level": 3, "health": 100},
    "Sam": {"level": 2, "health": 80},
}

# Read from left to right: find Sam, then find Sam's health.
print("\nSam's health:", players["Sam"]["health"])

players["Sam"]["health"] += 10
print("After healing:", players["Sam"]["health"])

for name, stats in players.items():
    print(f"{name} is level {stats['level']}")

# ==================================================
# 4 - A List of Dictionaries
# ==================================================

# A list works well when you want a sequence of similar records.
games = [
    {"title": "Minecraft", "rating": 9},
    {"title": "Rocket League", "rating": 8},
    {"title": "Stardew Valley", "rating": 10},
]

print("\nHighly rated games:")
for game in games:
    if game["rating"] >= 9:
        print(game["title"])

# ==================================================
# 5 - Add Up Dictionary Values
# ==================================================

scores = {"Alex": 120, "Sam": 90, "Jordan": 150}
total = 0

for score in scores.values():
    total += score

print("\nTotal score:", total)
print("Average score:", total / len(scores))
# This dictionary has entries. An empty dictionary would have length 0,
# so check that it is not empty before calculating an average.

# ==================================================
# 6 - Count Repeated Items
# ==================================================

loot = ["coin", "gem", "coin", "potion", "gem", "coin"]
counts = {}

for item in loot:
    # A new item starts at 0; an existing item keeps its current count.
    counts[item] = counts.get(item, 0) + 1

print("\nLoot counts:", counts)
# Expected: {'coin': 3, 'gem': 2, 'potion': 1}

"""
Quick reminders:
- update() can change or add several pairs.
- Dictionary values can be lists or other dictionaries.
- Use one pair of brackets for each level you access.
- items() gives both the key and value in a loop.
- get(key, 0) is useful when counting something for the first time.

Next: try more_dictionaries_practice.py!
"""
