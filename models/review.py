#!/usr/bin/python3
"""This module contains the definition of the Review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This is the Review class that inherits from BaseModel.

    Attributes:
        place_id (str): Place.id
        user_id (str): User.id
        text (str): text
    """

    place_id = ""
    user_id = ""
    text = ""
