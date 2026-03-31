# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import function

# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))   # Max combat strength is 6
big_dice_options = list(range(1, 21))    # Max health points is 20

# Define the number of stars to award the player
num_stars = 0

# ---------------------------
# INPUTS with try/except
# ---------------------------
i = 0
input_valid = False

# Hero combat strength
while not input_valid and i in range(5):
    try:
        combat_strength = int(input("Enter your combat Strength (1-6): "))
        if combat_strength not in range(1, 7):
            print("Enter a valid integer between 1 and 6 only")
            i += 1
        else:
            input_valid = True
    except:
        print("Invalid input. Player needs to enter integer numbers for Combat Strength")
        i += 1

m_input_valid = False

# Monster combat strength (user input step, even though later we roll monster strength)
while not m_input_valid and i in range(5):
    try:
        m_combat_strength = int(input("Enter the monster's combat Strength (1-6): "))
        if m_combat_strength not in range(1, 7):
            print("Enter a valid integer between 1 and 6 only")
            i += 1
        else:
            m_input_valid = True
    except:
        print("Invalid input. Monster needs to enter integer numbers for Combat Strength")
        i += 1

# If too many bad attempts, exit
if not (input_valid and m_input_valid):
    print("Too many invalid attempts. Exiting game.")
    quit()

# ---------------------------
# GAME SETUP
# ---------------------------

# Roll for player health points
input("Roll the dice for your health points (Press enter)")
health_points = random.choice(big_dice_options)
print("Player rolled " + str(health_points) + " health points")

# (TEST LINE from instructions - keep commented)
# health_points = function.monster_attacks("Somestring1", "Somestring2")

# Roll for monster combat strength (actual game roll)
input("Roll the dice for the monster's combat strength (Press enter)")
m_combat_strength = random.choice(small_dice_options)
print("Player rolled " + str(m_combat_strength) + " combat strength for the monster")

# Roll for monster health points
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(big_dice_options)
print("Player rolled " + str(m_health_points) + " health points for the monster")

# ---------------------------
# FIGHT LOOP
# ---------------------------
while m_health_points > 0 and health_points > 0:
    # Who attacks first?
    input("Roll to see who attacks first (Press Enter)")
    attack_roll = random.choice(small_dice_options)

    if not (attack_roll % 2 == 0):
        # Hero attacks first
        input("You strike (Press enter)")
        m_health_points = function.hero_attacks(combat_strength, m_health_points)

        if m_health_points != 0:
            input("The monster strikes (Press enter)!!!")

            # Monster attacks (try/except required)
            try:
                health_points = function.monster_attacks(m_combat_strength, health_points)
            except Exception as e:
                print("Custom error: monster_attacks() failed because values were not integers.")
                print("Details:", e)
                health_points = 0

    else:
        # Monster attacks first
        input("The Monster strikes (Press enter)")

        # Monster attacks (try/except required)
        try:
            health_points = function.monster_attacks(m_combat_strength, health_points)
        except Exception as e:
            print("Custom error: monster_attacks() failed because values were not integers.")
            print("Details:", e)
            health_points = 0

        if health_points != 0:
            input("The hero strikes!! (Press enter)")
            m_health_points = function.hero_attacks(combat_strength, m_health_points)

# ---------------------------
# END RESULT
# ---------------------------
if health_points <= 0:
    print("\nGame Over: The monster won.")
else:
    print("\nVictory: You defeated the monster!")