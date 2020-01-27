#!/usr/bin/python3
""" --- """

from models.base import Base


class Rectangle(Base):
    """ --- """
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
        """ --- """
        return self.__width

    @width.setter
    def width(self, val):
        """ --- """
        self.valwh("width", val)
        self.__width = val

    @property
    def height(self):
        """ --- """
        return self.__height

    @height.setter
    def height(self, val):
        """ --- """
        self.valwh("height", val)
        self.__height = val

    @property
    def x(self):
        """ --- """
        return self.__x

    @x.setter
    def x(self, val):
        """ --- """
        self.valxy("x", val)
        self.__x = val

    @property
    def y(self):
        """ --- """
        return self.__y

    @y.setter
    def y(self, val):
        """ --- """
        self.valxy("y", val)
        self.__y = val

    def valxy(self, name, val):
        """ --- """
        if type(val) is not int:
            raise TypeError(name + " must be an integer")
        if val < 0:
            raise ValueError(name + " must be >= 0")

    def valwh(self, name, val):
        """ --- """
        if type(val) is not int:
            raise TypeError(name + " must be an integer")
        if val <= 0:
            raise ValueError(name + " must be > 0")

    def area(self):
        """ --- """
        return self.__height * self.__width

    def display(self):
        """ --- """
        for i in range(self.__height):
            print("#"*self.__width)

    def __str__(self):
        """ --- """
        return "[" + __class__.__name__ + "] (" + str(self.id) + ") " + \
               str(self.__x) + "/"+str(self.__y) + " - " + \
               str(self.__width) + "/" + str(self.__height)

    def display(self):
        """ --- """
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" "*self.__x + "#"*self.__width)

    def update(self, *args, **kwargs):
        """ --- """
        if len(args) > 0:
            i = 0
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]

    def to_dictionary(self):
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
