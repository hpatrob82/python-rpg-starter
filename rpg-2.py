# Step 2
# Take the code for the hero attacking the goblin and extract it into a method (call it attack) of the Hero class.

# Replace the existing code with a call to the attack method.

# Hint: attack should take in the goblin (enemy) as a parameter: hero.attack(goblin)

class Hero:
    def __init__(self, health=10, power=5):
        self.health = health
        self.power = power
    def attack(self, enemy):
        enemy.health -= self.power
        print("You do %d damage to the hero." % self.power)
        if enemy.health <= 0:
            print("The hero is dead.")

class Goblin:
    def __init__(self, health=6, power=2):
        self.health = health
        self.power = power

        
def main():
    hero = Hero()
    goblin = Goblin()


    while goblin.health and hero.health:
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")


main()