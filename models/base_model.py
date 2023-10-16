#!/usr/bin/python3
"""Base mode class that has common properties."""
from datetime import datetime
import uuid
import models


class BaseModel:
    """Base model.

    common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """Initialise base class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            self.id = kwargs["id"]
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            models.storage.new(self)

    def __str__(self):
        """Return string representation of `BaseModel` class."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save object and update `updated_at`."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert object to dictionary."""
        d = self.__dict__.copy()
        d["__class__"] = type(self).__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return
