#!/usr/bin/python3
"""FileStorage Module."""
import json
from pathlib import Path
from typing import Any
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class.

    Class that serializes / deserializes instances
    """

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """Return all `__objects`.

        Returns:
                Dictionary of objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Set new object.

        Args:
            obj (`any`): object to be stored
        """
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize `__objects` to the JSON file."""
        serialize_objects = {obj: FileStorage.__objects[obj].to_dict()
                             for obj in FileStorage.__objects.keys()}
        path = Path(FileStorage.__file_path)
        path.write_text(json.dumps(serialize_objects))

    def reload(self):
        """Reload object from json file"""
        p = Path("file.json")
        if p.exists():
            data = json.loads(p.read_text())
            for value in data.values():
                obj = globals()["BaseModel"](**value)
                for key in value.keys():
                    if key not in obj.to_dict().keys():
                        setattr(obj, key, value[key])
                self.new(obj)
