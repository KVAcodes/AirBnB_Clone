#!/usr/bin/python3
"""This module contains the BaseModel class definition.
"""

import uuid
import datetime
import models

class BaseModel:
    """The BaseModel class defines the all common attributes/methods for other
    classes
    """
    def __init__(self, *args, **kwargs):
        """Initializer/constructor of the BaseModel class.

        Args:
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """returns a human-readable/informal string representation of the
        BaseModel object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute 'updated_at' with the current
        datetime.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the
        instance.
        """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['created_at'] = new_dict['created_at'].isoformat()

        return new_dict
