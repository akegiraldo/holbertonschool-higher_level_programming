#!/usr/bin/python3


class MyInt(int):
    def __init__(self, y):
        self.y = y

    def __eq__(self, other):
        return (not self.y == other)

    def __ne__(self, other):
        return (not self.y != other)
