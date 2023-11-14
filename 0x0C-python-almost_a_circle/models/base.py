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
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Gets instances of attributes set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
                dummy.update(**dictionary)
            return (dummy)

    @classmethod
    def load_from_file(cls):
        """"""
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                list_instances = []

                for d in list_dicts:
                    list_instances.append(cls.create(**d))
                return (list_instances)
        except fileNotFoundError:
            return([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Gets CSV serialization of an object list to a file"""
        file_name = "{}.json".format(cls.__name__)

        with open(file_name, "w") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)

            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Gets list of class instances from CSV file"""
        file_name = "{}.json".format(cls.__name__)

        try:
            with open(file_name, "r") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)

                nw_list_dict = []
                convertd_dict = {}

                for c in list_dicts:
                    for key, value in c.items():
                        convert_dict[key] = int(value)

                        n_list_dicts = n_list_dict

                        list_of_instances = []

                        for c in list_dicts:
                            list_of_instances.append(cls.create(**d))

                    return (list_of_instances)

        except FileNotFoundError:
            return ([])

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
