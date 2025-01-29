import random

# Step 1: Define Monster's Powers
defined_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Step 2: Roll for Monster's Magic Power
selected_power = random.choice(list(defined_powers.keys()))
print(f"The monster has rolled the power: {selected_power}")

# Step 3: Update Monster's Combat Strength
m_combat_strength = random.randint(1, 6)  # Initial random strength
m_combat_strength += defined_powers[selected_power]
m_combat_strength = min(6, m_combat_strength)
print(f"Updated combat strength: {m_combat_strength} (Power: {selected_power})")

# Step 4: Define Loot Belt
belt = []
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]

good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]

# Step 5: Collect First Loot Item
print("You have found a loot bag!")
input("Press Enter to roll for the first loot item.")
loot_item = loot_options.pop(random.randint(0, len(loot_options) - 1))
belt.append(loot_item)
print(f"Added {loot_item} to your belt. Current belt: {belt}")

# Step 6: Collect Second Loot Item
input("Press Enter to roll for the second loot item.")
loot_item = loot_options.pop(random.randint(0, len(loot_options) - 1))
belt.append(loot_item)
print(f"Added {loot_item} to your belt. Current belt: {belt}")

# Step 7: Organize the Loot Belt
print("Organizing the belt alphabetically...")
belt.sort()
print(f"Organized belt: {belt}")

# Step 8: Use the First Loot Item
health_points = random.randint(1, 6)  # Initial player health
if belt:
    print("You see a monster in the distance. Use the first item in your belt!")
    used_item = belt.pop(0)
    if used_item in good_loot_options:
        health_points = min(6, health_points + 2)
        print(f"Used {used_item}. Health increased to {health_points}.")
    elif used_item in bad_loot_options:
        health_points = max(0, health_points - 2)
        print(f"Used {used_item}. Health decreased to {health_points}.")
    else:
        print(f"Used {used_item}. It was not helpful.")
else:
    print("Your belt is empty!")
