#!/usr/bin/python3

"""
a module for the Base class
"""
import json
import csv
import turtle
import tkinter as TK


class Base:
    """
    Attributes:
        __nb_objects - a private class attr. Default = 0
    Notes:
        This class is the base of all other class in this project. The goal
        is to manage id's of all the future class and avoid duplicating code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Notes:
            This is a class constructor that manages classes  id
        Parameters:
            id - class id for future class. Default = None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Note:
            json string representations for the dictionaries
        Return:
            json string for dictionary or [] if dict not exist
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Parameters:
            list_objs (list): List of instances inheriting from Base.

        Returns:
            None
        """
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dicts)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string.

        Parameters:
            json_string (str): String representing a list of dictionaries.

        Returns:
            list: List represented by json_string.
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set.

        Parameters:
            **dictionary (dict): Double pointer to a dictionary.

        Returns:
            Base: Instance with attributes set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance

        dummy_instance.update(**dictionary)  # Update with real val from dict
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**obj_dict) for obj_dict in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize instances to a CSV file.

        Parameters:
            list_objs (list): List of instances.

        Returns:
            None
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height,
                                    obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from a CSV file.

        Returns:
            list: List of instances.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                list_objs = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj_dict = {
                            'id': int(row[0]),
                            'width': int(row[1]),
                            'height': int(row[2]),
                            'x': int(row[3]),
                            'y': int(row[4])
                        }
                    elif cls.__name__ == "Square":
                        obj_dict = {
                            'id': int(row[0]),
                            'size': int(row[1]),
                            'x': int(row[2]),
                            'y': int(row[3])
                        }
                    list_objs.append(cls.create(**obj_dict))
                return list_objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Open a window and draw all Rectangles and Squares.

        Parameters:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.

        Returns:
            None
        """
        screen = turtle.Screen()
        screen.bgcolor("white")
        pen = turtle.Turtle()

        def draw_shape(obj, color):
            pen.color(color)
            pen.penup()
            pen.goto(obj.x, obj.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(obj.width if hasattr(obj, 'width') else obj.size)
                pen.left(90)

        for rectangle in list_rectangles:
            draw_shape(rectangle, "blue")

        for square in list_squares:
            draw_shape(square, "red")

        turtle.done()
