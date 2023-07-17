#!/usr/bin/python3
"""This module contains the definition of the Amenity class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the Amenity class that inherits from BaseModel.

    Attributes:
        name (str): name
    """

    name = ""
