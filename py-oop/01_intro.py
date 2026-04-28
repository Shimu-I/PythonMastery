# object = A "bundle" of related attributes (variable) and method (functions)
#           Ex. phone, cup, book
#           You need a "class" to create many object
# class = (blueprint) used to design the structure and layout of an object


from car import Car


car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)


print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print("=" * 20)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print("="* 20)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

print("="* 20)

car1.drive()
car2.drive()
car3.drive()
car1.describe()
car2.describe()
car3.describe()



# car1. # attribute access operator
# self  # the object we are currently working with