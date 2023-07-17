#!/usr/bin/python3
"""This module contains the FileStorage class definition.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """This is the FileStorage class that serializes instances to a JSON file
    and deserializes JSON file to instances.
    """

    __file_path = "file.json"  #: path to the JSON file
    #: dictionary: dictionary - empty but will store all objects by
    # <class name>.id (ex: to store a BaseModel object with id=12121212,
    # the key will be BaseModel.12121212)
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return self.__class__.__objects

    def new(self, obj):
        """sets in __objects the obj with key "<obj class name>.id".
        """
        self.__class__.__objects[f"{obj.__class__.__name__}"
                                 f".{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__class__.__file_path, "w") as storage_file:
            tmp_dict = {key: value.to_dict() for key, value in
                        self.__class__.__objects.items()}
            json.dump(tmp_dict, storage_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, it does nothing.
        """

        try:
            with open(self.__class__.__file_path, "r") as storage_file:
                tmp_dict = json.load(storage_file)
                self.__class__.__objects = {key: eval(value['__class__'])
                                            (**value)for key, value in
                                            tmp_dict.items()}
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return
