#!/usr/bin/python3
"""
Serializes instances to a JSON file
Deserializes JSON file to instances:
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """ serializes instances to a JSON file and deserializes JSON file"""

    __file_path = "file.json"  # path to the JSON file (ex: file.json)
    __objects = {}  # dictionary - stores all objects by <class name>.id

    def all(self):
        """  returns dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        # get key of the form <obj class name>.id
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        # create empty dictionary
        json_object = {}

        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as file_name:
            json.dump(json_object, file_name)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as file_name:
                for key, value in json.load(file_name).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass
