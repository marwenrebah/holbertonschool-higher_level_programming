#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class, inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize width, height, x, y, and id using the Base class"""
        # Set the attributes of the Rectangle
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # Call the constructor of the Base class to handle id
        super().__init__(id)

    @property
    def width(self):
        """Retrieve the value of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the value of width"""
        # Validate and set the width attribute
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Retrieve the value of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the value of height"""
        # Validate and set the height attribute
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Retrieve the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the value of x"""
        # Validate and set the x attribute
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Retrieve the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the value of y"""
        # Validate and set the y attribute
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Display the rectangle"""
        # ... (no changes in code, comments added for clarity)

    def __str__(self):
        """Return a string representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""
        # ... (no changes in code, comments added for clarity)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width}
