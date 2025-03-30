
# class = A "Bundle" of related attributes ((variables ))  and methods (functions)
# You need class to handle many objects 

# Class = Blueprint of the , used to design the structure of the object


# 3 SUPER  = The super() function is used to give access to methods and properties of a parent or sibling class.

            # The super() function returns an object that represents the parent class.



class shapes:
    def __init__(self,colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def message(self):
        print(f"The colour is {self.colour}, and {"filled" if self.is_filled else 'not filled' }")

class circle (shapes):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

class triangle(shapes):
    def __init__(self, colour, is_filled, height):
        super().__init__(colour, is_filled)
        self.height = height

triangle1 = triangle(colour="red", is_filled= True, height= "45")

triangle1.message()

#  output
# The colour is red, and filled  

        