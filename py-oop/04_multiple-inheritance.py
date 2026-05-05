# multiple inheritance = inherit form more than one parent class 
#                        C(A, B)
# multilevel inheritance = inherit form a parent which inherits from another parent 
#                        C(B) <- B(A) <- A


## MULTIPLE INHERITANCE
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

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


rabbit.flee()
hawk.hunt()
#hawk.flee()
fish.flee()
fish.hunt()


print("=" * 30)

rabbit.eat()
rabbit.sleep()
fish.eat()
fish.sleep()

print("=" * 30)

rabbit.eat()
rabbit.sleep()
rabbit.flee()

print("=" * 30)

hawk.eat()
hawk.sleep()
hawk.hunt()

print("=" * 30)

fish.eat()
fish.sleep()
fish.flee()
fish.hunt()