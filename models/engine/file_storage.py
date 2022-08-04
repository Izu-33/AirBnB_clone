#!/usr/bin/python3
"""Defines FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """Represents a a storage engine.

    Attributes:
        __file_path (str): path to JSON file.
        __objects (dict): dictionary to store all objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects[class_name + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        all_objects = FileStorage.__objects
        obj_dict_str = {k: v.to_dict() for k, v in all_objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict_str, f)

    def reload(self):
        """Deserializes he JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict_str = json.load(f)
                for obj in obj_dict_str.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
