#!/usr/bin/python3
"""Defines unittests for models/base_model.py

Unittest classes:
    TestBaseModel_init
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel_init(unittest.TestCase):
    """Tests for instantiation of BaseModel class."""

    def test_init_with_no_args(self):
        self.assertEqual(type(BaseModel()), BaseModel)

    def test_id_is_public_str(self):
        self.assertEqual(type(BaseModel().id), str)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(type(BaseModel().created_at), datetime)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(type(BaseModel().updated_at), datetime)

    def test_unique_ids_for_two_models(self):
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_different_created_at_two_models(self):
        base_model_1 = BaseModel()
        sleep(0.05)
        base_model_2 = BaseModel()
        self.assertLess(base_model_1.created_at,
                        base_model_2.created_at)

    def test_different_updated_at_two_models(self):
        base_model_1 = BaseModel()
        sleep(0.05)
        base_model_2 = BaseModel()
        self.assertLess(base_model_1.updated_at,
                        base_model_2.updated_at)

    def test_str_repr(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        base_model_1 = BaseModel()
        base_model_1.id = "123456"
        base_model_1.created_at = base_model_1.updated_at = dt
        base_model_str = base_model_1.__str__()
        self.assertIn("[BaseModel] (123456)", base_model_str)
        self.assertIn("'id': '123456'", base_model_str)
        self.assertIn("'created_at': " + dt_repr, base_model_str)
        self.assertIn("'updated_at': " + dt_repr, base_model_str)

    def test_unused_args(self):
        base_model_1 = BaseModel(None)
        self.assertNotIn(None, base_model_1.__dict__.values())

    def test_init_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        base_model_1 = BaseModel(id="123456", created_at=dt_iso,
                                    updated_at=dt_iso)
        self.assertEqual(base_model_1.id, "123456")
        self.assertEqual(dt, base_model_1.created_at)
        self.assertEqual(dt, base_model_1.updated_at)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_to_dict_datetime_attrs_are_str(self):
        base_model_1 = BaseModel()
        base_model_dict = base_model_1.to_dict()
        self.assertEqual(type(base_model_dict["created_at"]), str)
        self.assertEqual(type(base_model_dict["updated_at"]), str)

    def test_contrast_to_dict_dunder_dict(self):
        base_model_1 = BaseModel()
        self.assertNotEqual(base_model_1.to_dict(),
                            base_model_1.__dict__)

    def test_to_dict_with_None_arg(self):
        base_model_1 = BaseModel()
        with self.assertRaises(TypeError):
            base_model_1.to_dict(None)


class TestBaseModel_save(unittest.TestCase):
    """Unittest for testing save method of the BaseModel class."""

    def test_different_updated_at_after_save(self):
        base_model_1 = BaseModel()
        sleep(0.05)
        prior_updated_at = base_model_1.updated_at
        base_model_1.save()
        self.assertLess(prior_updated_at, base_model_1.updated_at)

    def test_save_with_None_arg(self):
        base_model_1 = BaseModel()
        with self.assertRaises(TypeError):
            base_model_1.save(None)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittest for testing the to_dict BaseModel class method."""

    def test_to_dict_type(self):
        base_model_1 = BaseModel()
        self.assertEqual(type(base_model_1.to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        base_model_1 = BaseModel()
        self.assertIn("id", base_model_1.to_dict())
        self.assertIn("created_at", base_model_1.to_dict())
        self.assertIn("updated_at", base_model_1.to_dict())
        self.assertIn("__class__", base_model_1.to_dict())

    def test_to_dict_contains_added_attributes(self):
        base_model_1 = BaseModel()
        base_model_1.name = "ALX"
        base_model_1.number = 98
        self.assertIn("name", base_model_1.to_dict())
        self.assertIn("number", base_model_1.to_dict())


if __name__ == "__main__":
    unittest.main()
