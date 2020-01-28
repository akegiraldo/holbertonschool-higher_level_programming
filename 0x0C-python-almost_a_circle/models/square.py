#!/usr/bin/python3
""" --- """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ --- """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        super().valwh("width", val)
        self.width = val
        self.height = val

    def __str__(self):
        """ --- """
        return "[" + __class__.__name__ + "] (" + str(self.id) + ") " +\
               str(self.x) + "/" + str(self.y) + " - " + str(self.width)

    def update(self, *args, **kwargs):
        """ --- """
        if len(args) > 0:
            i = 0
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """ --- """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    @staticmethod
    def to_json_string(list_dictionaries):
        """ --- """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ --- """
        filename = "" + cls.__name__ + ".json"
        ls = []
        with open(filename, mode='w', encoding='UTF-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            else:
                for i in list_objs:
                    ls.append(i.to_dictionary())
                json_list = cls.to_json_string(ls)
            return f.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """ --- """
        if json_string is None or len(json_string) <= 0:
            return []
        return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ --- """
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        elif cls.__name__ == "Square":
            tmp = cls(560)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """ --- """
        h = "" + cls.__name__ + ".json"
        text = ""
        newlist = []
        if os.path.exists(h) is False:
            return []
        with open(h, "r", encoding="UTF-8") as f:
            text = f.read()
            obj = cls.from_json_string(text)
            for i in obj:
                newlist.append(cls.create(**i))
        return newlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ --- """
        filename = "" + cls.__name__ + ".csv"
        ls = []
        with open(filename, mode='w', encoding='UTF-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            else:
                for i in list_objs:
                    ls.append(i.to_dictionary())
                json_list = cls.to_json_string(ls)
            return f.write(json_list)

    @classmethod
    def load_from_file_csv(cls):
        """ --- """
        h = "" + cls.__name__ + ".csv"
        text = ""
        newlist = []
        if os.path.exists(h) is False:
            return []
        with open(h, "r", encoding="UTF-8") as f:
            text = f.read()
            obj = cls.from_json_string(text)
            for i in obj:
                newlist.append(cls.create(**i))
        return newlist
