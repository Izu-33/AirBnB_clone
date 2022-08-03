#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v,
                                                         time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        repr_dict = self.__dict__.copy()
        repr_dict["created_at"] = self.created_at.isoformat()
        repr_dict["updated_at"] = self.updated_at.isoformat()
        repr_dict["__class__"] = self.__class__.__name__
        return repr_dict

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id,
                                     self.__dict__)
