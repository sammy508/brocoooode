
# static method = A method that belong to a class rathwer than any object from that class(instance) 
#           usually used for gegneral utility functions

# instance method = best for operation on instances of the class (objects)
# static method = best for utility that do not need access to class data


class Employee:

    def __init__(self, name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod

    def is_valid_position(position):
        valid_position =["astronaut","Plumber","Doctor","Gym Trainer"]
        return position in valid_position

  # static methods  
print(Employee.is_valid_position("astronaut"))

# for instance method

emp1 = Employee("JOnny","Doctor")
print(emp1.get_info())


