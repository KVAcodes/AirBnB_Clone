#!/usr/bin/python3
"""This module contains the FileStorage class definition.
"""

import json
from models.base_model import BaseModel

class FileStorage:
    """This class serializes instances to a JSON file and deserializes
    JSON file to instances.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """sets in {_objects} the {obj} with the key <obj class name>.id

        Args:
            obj(BaseModel): The object to store within __objects dict
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file in the path: __file_path.
        """
        with open(self.__file_path, "w") as json_file:
            serial_dict = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(serial_dict, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file in
        (__file_path) exists.
        """

        try:
            with open(self.__file_path, "r") as json_file:
                tmp_dict = json.load(json_file)
                self.__objects = {key: eval(value['__class__'])(**value) for key,
                                  value in tmp_dict.items()}
        except FileNotFoundError:
            return
