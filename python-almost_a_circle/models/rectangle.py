#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """this is the class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize width,height,x,y and id
        super() is a builtin function that allow us to acces
        method of the Base class and then we can initialize
        id using __init__because id is a part of Base
        not Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve value of width """
        return self.__width

    @width.setter
    def width(self, width):
        """set value to width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """retrieve value of height """
        return self.__height

    @height.setter
    def height(self, height):
        """set value to height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """retrieve value of x """
        return self.__x

    @x.setter
    def x(self, x):
        """set value to x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """retrieve value of y """
        return self.__y

    @y.setter
    def y(self, y):
        """set value to y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """calculate the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """display the rectangle"""
        if self.__y > 0:
            for i in range(self.__y):
                print()
        for i in range(self.__height):
            if self.__x > 0:
                for i in range(self.__x):
                    print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """[Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            elif len(args) >= 2:
                self.__width = args[1]
            elif len(args) >= 3:
                self.__height = args[2]
            elif len(args) >= 4:
                self.__x = args[3]
            elif len(args) >= 5:
                self.__y = args[4]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """return the dictionary representation of a Rectangle"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width}
