import random

# -----------------------------
# Question 1 – Monster Powers
# -----------------------------
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Starting monster combat strength
m_combat_strength = 2

# -----------------------------
# Question 2 – Roll for Magic
# -----------------------------
input("Press Enter to roll for the monster's magic power...")

rolled_power = random.choice(list(monster_powers.keys()))
print("Monster rolled:", rolled_power)

# -----------------------------
# Question 3 – Update Combat Strength
# -----------------------------
m_combat_strength += monster_powers[rolled_power]

# Ensure max combat strength is 6
m_combat_strength = min(m_combat_strength, 6)

print("Updated monster combat strength:", m_combat_strength)

# -----------------------------
# Question 4 – Loot Setup
# -----------------------------
loot_options = ["Potion", "Sword", "Shield", "Poison", "Rock"]
good_loot = ["Potion", "Shield"]
bad_loot = ["Poison"]

belt = []

health_points = 4

# -----------------------------
# Question 5 – First Loot Item
# -----------------------------
print("\nYou found a loot bag!")
input("Press Enter to roll for your first item...")

item1 = random.choice(loot_options)
loot_options.pop(loot_options.index(item1))
belt.append(item1)

print("Belt now contains:", belt)

# -----------------------------
# Question 6 – Second Loot Item
# -----------------------------
input("\nPress Enter to roll for your second item...")

item2 = random.choice(loot_options)
loot_options.pop(loot_options.index(item2))
belt.append(item2)

print("Belt now contains:", belt)

# -----------------------------
# Question 7 – Organize Belt
# -----------------------------
print("\nOrganizing belt alphabetically...")
belt.sort()
print("Organized belt:", belt)

# -----------------------------
# Question 8 – Use First Loot
# -----------------------------
print("\nYou see a monster in the distance!")
print("Using first item in your belt...")

used_item = belt.pop(0)
print("Used item:", used_item)

if used_item in good_loot:
    health_points += 2
    health_points = min(health_points, 6)
elif used_item in bad_loot:
    health_points -= 2
    health_points = max(health_points, 0)
else:
    print("Item was not helpful.")

print("Player health points:", health_points)
