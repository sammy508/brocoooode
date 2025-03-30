
# @property = Decorator used to define a method as a property (it can be accessed like a attribute)
        # Benefit : Add additional logic when read, write or delete attributes
    # Gives us a setter, getter and deleter method


class Rectangel:
    def __init__(self, width, height):
        self._width = width   # protected variable
        self._height = height

    @property

    def width(self):
        return f"{self._width} cm"
    
    @width.setter
    def width(self,new_width):
        if new_width > 0 :
            self._width = new_width
        else:
            print("Width must be greater than 0")

Rectangel.width =5
rectangel1 = Rectangel(3, 4)
    
print(rectangel1.width)

