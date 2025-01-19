import random

#
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]


try:
    weaponRoll = random.randint(1, 6)  # Rolling dice (1-6)
    print(f"Weapon Roll: {weaponRoll}")


    hero_combat_strength = 10 + weaponRoll
    print(f"Hero's combat strength: {hero_combat_strength}")


    hero_weapon = weapons[weaponRoll - 1]
    print(f"Hero's Weapon: {hero_weapon}")


    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    if hero_weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

except Exception as e:
    print("Error:", e)
