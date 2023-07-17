#!/usr/bin/python3
"""This module contains the definition of the State class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """This is the State class that inherits from BaseModel.

    Attributes:
        name (str): state name
    """

    name = ""
