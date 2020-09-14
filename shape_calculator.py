''' 
    Author: Xiana Carrera Alonso
    Date: 24/08/2020
    This is a program made for the 'Scientific Computing with Python' course of freeCodeCamp.
    This code corresponds to the fourth assigment, 'Polygon Area Calculator'.
    The purpose of the code is to 'to create a Rectangle class and a Square class'
    where the Square class is a subclass of the Rectangle class and inherits methods and attributes. 
    Complete instructions for this assigment can be found at
    https://repl.it/@freeCodeCamp/fcc-shape-calculator#README.md
'''

class Rectangle:

    def __init__(self, w, h):
        self.width = w
        self.height = h
        
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    
    def set_width(self, w):
        self.width = w
    
    def set_height(self, h):
        self.height = h
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
        
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5   # Pythagorean theorem
        
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ""
        # self.width or self.height are converted to integers in case they were passed as floating point numbers
        for i in range(int(self.height)):
            for j in range(int(self.width)):
                picture += "*"
            picture += "\n"
        
        return picture
    
    def get_amount_inside(self, shape):
        # Calculates how many times the passed shape would fit into the object
        # No rotations are allowed
        amount = 0      # The answer may be 0 if shape is too big
        for i in range(int(self.height) // int(shape.height)):  
            for j in range(int(self.width) // int(shape.width)):
                amount += 1
        return amount


class Square(Rectangle):
    
    def __init__(self, s):
        self.width = s 
        self.height = s
        
    def __str__(self):
        return "Square(side=" + str(self.width) + ")"
        
    def set_side(self, s):
        self.width = s
        self.height = s   
        
    def set_width(self, w):     # Needs to be overriden
        self.set_side(w)
    
    def set_height(self, h):    # Needs to be overriden
        self.set_height(h)
    
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
 
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
 
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
