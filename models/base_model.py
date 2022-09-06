#!/usr/bin/python3
"""
    Creating the base class for all other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
        This is the base class for managing attributes of all other classes
    """

    def __init__(self, *args, **kwargs):
        """ Public instance artributes initialization """

        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    setattr(self,
                            key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            Method to return string representation of objects
        """
        return ("[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
            ))

    def save(self):
        """
            Method to update  public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
           Returns dictionary containing all keys/values
           of __dict__ of the instance
        """

        dict_ = self.__dict__.copy()
        dict_['__class__'] = self.__class__.__name__
        dict_['created_at'] = dict_['created_at'].isoformat()
        dict_['updated_at'] = dict_['updated_at'].isoformat()

        return dict_
