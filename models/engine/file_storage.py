#!/usr/bin/python3
"""FileStorage Module."""
import json
from pathlib import Path
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
        serialize_objects = {obj : FileStorage.__objects[obj].to_dict()
                             for obj in FileStorage.__objects.keys()}
        path = Path(FileStorage.__file_path)
        path.write_text(json.dumps(serialize_objects))

    def reload(self):
        """Reload object from json file"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name))
        except FileNotFoundError:
            return

