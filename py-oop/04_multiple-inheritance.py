# multiple inheritance = inherit form more than one parent class 
#                        C(A, B)
# multilevel inheritance = inherit form a parent which inherits from another parent 
#                        C(B) <- B(A) <- A


## MULTIPLE INHERITANCE

class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit:
    pass

class Hawk:
    pass

class Fish:
    pass