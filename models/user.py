#!/usr/bin/python3
"""This module contains the definition of the User class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """This is the User class that inherits from BaseModel.

    Attributes:
        email (str): The email address of the user
        password (str): The password of the user
        first_name (str): The user's Firstname
        last_name (str): The user's Lastname
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
