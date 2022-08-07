#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_init
    TestFileSTorage_methods
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestFileStorage_init(unittest.TestCase):
    """Unittests for FileStorage class instantiation."""

    def test_FileStorage_init_with_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_init_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_FileStorage_objects_is_private_dict(self):
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for methods of FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except (OSError, IOError):
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except (FileNotFoundError, IOError):
            pass

        try:
            os.rename("tmp", "file.json")
        except (OSError, IOError):
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(type(models.storage.all()), dict)

    def test_all_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base_model_1 = BaseModel()
        models.storage.new(base_model_1)
        self.assertIn("BaseModel." + base_model_1.id,
                      models.storage.all().keys())
        self.assertIn(base_model_1, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        base_model_1 = BaseModel()
        models.storage.new(base_model_1)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_model_1.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        base_model_1 = BaseModel()
        models.storage.new(base_model_1)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model_1.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
