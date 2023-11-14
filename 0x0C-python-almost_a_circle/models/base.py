#!/usr/bin/python3
"""Module defines a base model class"""
from json import dumps, loads
import csv
import turtle


class Base:
    """Representation of a base model
    With private class atributes giving nmber of instances"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Defines a list represrentation of a dictionary list"""
        if list_dictionaries is None or not list_dictionaries:
            return ("[]")
        else:
            return (dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Gets a JSON string representation with args list to a file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    def from_json_string(json_string):
        """Gets the list represented by the json string"""
        if json_string is None or json_string == "[]":
            return ([])
        return (loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Gets instances of attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Loads into csv file"""
        fName = str(cls.__name__) + ".json"
        try:
            with open(fName, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return ([cls.create(**d) for d in list_dicts])
        except IOError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Gets CSV serialization of an object list to a file"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]
        with open("{}.csv".format(cls.__name__), "w", newline="",
                  encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Gets list of class instances from CSV file"""
        from models.rectangle import Rectangle
        from models.square import Square
        ip = []
        with open("{}.csv".format(cls.__name__), "r", newline="",
                  encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ip.append(cls.create(**d))
        return (ip)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all rectangles and squares using turtle module"""
        turt = turtle.Turtle()

        turt.screen.bgcolor("#3399FF")

        turt.pensize(4)

        turt.shape("turtle")

        for rect in list_rectangles:
            turt.showturtle()

            turt.up()

            turt.goto(rect.x, rect.y)

            turt.down()

            for _ in range(2):
                turt.forward(rect.width)

                turt.left(90)

                turt.forward(rect.height)

                turt.left(90)

            turt.hideturtle()

        turt.color("#4682B4")

        for sqr in list_squares:
            turt.showturtle()

            turt.up()

            turt.goto(sqr.x, sqr.y)

            turt.down()

            for _ in range(2):
                turt.forward(sqr.width)
                turt.left(90)

                turt.forward(sqr.height)

                turt.left(90)

            turt.hideturtle()

        turtle.exitonclick()


if __name__ == "__main__":

    pass
