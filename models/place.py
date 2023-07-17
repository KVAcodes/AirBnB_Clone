#!/usr/bin/python3
"""This module contains the definition of the Place class.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """This is the Place class that inherits from BaseModel.

    Attributes:
        city_id (str): city.id
        user_id (str): user.id
        name (str): name of place
        description (str): description of place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guests
        price_by_night (int): price by night
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (list of str): list of Amenity.id

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0)
    longitude = float(0)
    amenity_ids = []
