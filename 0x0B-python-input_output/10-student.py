#!/usr/bin/python3
"""
    student file
"""

class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None):
        all_attributes = self.__dict__.copy()

        if attributess and isinstance(attributes, list):
            for key in self.__dict__.keys():
                if key not in attributes:
                    del all_attributes[key]
        return all_attributes
