#!/usr/bin/python3
"""This module contains the definition of the City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """This is the City class that inherits from BaseModel.

    Attributes:
        state_id (str): state.id
        name (str): city name
    """

    state_id = ""
    name = ""
