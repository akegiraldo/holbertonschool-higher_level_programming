#!/usr/bin/python3


from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.valwh("width", width)
        self.width = width
        self.valwh("height", height)
        self.height = height
        self.valxy("x", x)
        self.x = x
        self.valxy("y", y)
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        self.valwh("width", val)
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.valwh("height", val)
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.valxy("x", val)
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.valxy("y", val)
        self.__y = val

    def valxy(self, name, val):
        if type(val) is not int:
            raise TypeError(name + " must be an integer")
        if val < 0:
            raise ValueError(name + " must be >= 0")

    def valwh(self, name, val):
        if type(val) is not int:
            raise TypeError(name + " must be an integer")
        if val <= 0:
            raise ValueError(name + " must be > 0")

    def area(self):
        return self.__height * self.__width

    def display(self):
        for i in range(self.__height):
            print("#"*self.__width)

    def __str__(self):
        return "[" + __class__.__name__ + "] (" + str(self.id) + ") " + \
                str(self.__x) + "/"+str(self.__y) + " - " + \
                str(self.__width) + "/" + str(self.__height)
