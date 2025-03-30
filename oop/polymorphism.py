
# # Polymorphism = The word "polymorphism" means "many forms", 
# #                   and in programming it refers to methods/functions/operators with the 
# #                   same name that can be executed on many objects or classes. 

# # There are two ways to achive polymorphism

#     # 1. Inheritance : An object could be treated as of the same type of as parent class
#     # 2. Duck Typing : Objects must have necessary attributes / methods
#   Duck typing vaneko regular polymorphism method same function multiple class ma  copy paste 


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(Shape):  # class
    # constructor
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    

class triangle(Shape):

    def __init__(self, base, height):  # constructor of triangle class
            self.base = base
            self.height = height
        
    def area(self):
            return (self.base * self.height)/2
  

class pizza (circle):
     def __init__(self, radius, topping):
          super().__init__(radius)
          self.topping = topping


shapes = [triangle(5,4), circle(5), pizza(5,"peproni")]
for shape in shapes :
     print(shape.area())
    


