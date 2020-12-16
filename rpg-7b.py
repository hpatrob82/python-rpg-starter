class Character:
    def __init__(self, health=10, power=5):
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def attack(self, enemy):
        enemy.health -= self.power
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))
        


            
class Hero(Character):
    def __init__(self, health=10, power=5):
        super().__init__(10, 5)
    def attack(self, enemy):
        enemy.health -= self.power
        print("You do %d damage to the goblin." % self.power)
        if enemy.health <= 0:
            print("The goblin is dead.")
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))



class Goblin(Character):
    def __init__(self, health=6, power=2):
        super().__init__(6, 2)
    def attack(self, enemy):
        enemy.health -= self.power
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False    
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))


def main():
    hero = Hero()
    goblin = Goblin()


    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
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
            goblin.attack(hero)
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")


main()   