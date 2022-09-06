#!/usr/bin/python3
""" Class that inherits from base model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Inherits from base model """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
