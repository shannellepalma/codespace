class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Scavenger(Animal):
    def search(self):
        print(f"{self.name} is searching for leftovers")

class Hyena(Predator, Scavenger):
    pass

class Vulture(Scavenger, Prey):
    pass

hyena = Hyena("Ha-Ha")
vulture = Vulture("Victor")

vulture.flee()    
vulture.search() 