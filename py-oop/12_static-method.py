# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data


# Instance Method = methods that belong to individual object created form that class
# def get_info(self):
#     return f"{self.name} = {self.position}"

# Static methods =
# @staticmethod
# def km_to_miles(kilometers):
#     return kilometeres * 0.621371

# @ = decorador

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position
    
    
employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Rocket Scientist"))
print(employee1.get_info())

print(employee2.get_info())

print(employee3.get_info())
