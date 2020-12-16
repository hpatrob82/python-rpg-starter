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



class Zombie(Character):
    def __init__(self, health=, power= :
        super().__init__()
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
    zombie = Zombie()


    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks zombie
            hero.attack(zombie)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if zombie.health > 0:
            # Zombie attacks hero
            zombie.attack(hero)
            print("The zombie does %d damage to you." % zombie.power)
            if hero.health <= 0:
                print("You are dead.")


main()   