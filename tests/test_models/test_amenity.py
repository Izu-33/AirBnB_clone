#!/usr/bin/python3
"""Defines unittest for models/amenity.py.

Unittest classes:
    TestAmenity_init
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_init(unittest.TestCase):
    """Tests for instantiation of Amenity class."""

    def test_init_with_no_args(self):
        self.assertEqual(type(Amenity()), Amenity)

    def test_new_instance_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(type(Amenity().id), str)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(type(Amenity().created_at), datetime)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(type(Amenity().updated_at), datetime)

    def test_name_is_public_class_str(self):
        amenity_1 = Amenity()
        self.assertEqual(type(Amenity.name), str)
        self.assertIn("name", dir(amenity_1))

    def test_two_amenities_unique_ids(self):
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_two_amenities_different_created_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.created_at, amenity_2.created_at)

    def test_two_amenities_different_updated_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.updated_at, amenity_2.updated_at)

    def test_str_repr(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        amenity_1 = Amenity()
        amenity_1.id = "123456"
        amenity_1.created_at = amenity_1.updated_at = dt
        amenity_1_str = amenity_1.__str__()
        self.assertIn("[Amenity] (123456)", amenity_1_str)
        self.assertIn("'id': '123456'", amenity_1_str)
        self.assertIn("'created_at': " + dt_repr, amenity_1_str)
        self.assertIn("'updated_at': " + dt_repr, amenity_1_str)

    def test_unused_args(self):
        amenity_1 = Amenity(None)
        self.assertNotIn(None, amenity_1.__dict__.values())

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Tests for save method of of Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_different_updated_at_after_save(self):
        amenity_1 = Amenity()
        sleep(0.05)
        prior_updated_at = amenity_1.updated_at
        amenity_1.save()
        self.assertLess(prior_updated_at, amenity_1.updated_at)

    def test_save_with_None_arg(self):
        amenity_1 = Amenity()
        with self.assertRaises(TypeError):
            amenity_1.save(None)

    def test_save_updates_file_with_amenity(self):
        amenity_1 = Amenity()
        amenity_1.save()
        amenity_1_id = "Amenity." + amenity_1.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_1_id, f.read())


class TestCase_to_dict(unittest.TestCase):
    """Test of to_dict method of State class."""

    def test_to_dict_type(self):
        self.assertEqual(type(Amenity().to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        amenity_1 = Amenity()
        self.assertIn("id", amenity_1.to_dict())
        self.assertIn("created_at", amenity_1.to_dict())
        self.assertIn("updated_at", amenity_1.to_dict())
        self.assertIn("__class__", amenity_1.to_dict())

    def test_to_dict_contains_added_attrs(self):
        amenity_1 = Amenity()
        amenity_1.pet_name = "Danny"
        amenity_1.phone = "123456"
        self.assertEqual(amenity_1.pet_name, "Danny")
        self.assertIn("phone", amenity_1.to_dict())

    def test_to_dict_datetime_attrs_are_str(self):
        amenity_1 = Amenity()
        amenity_1_dict = amenity_1.to_dict()
        self.assertEqual(type(amenity_1_dict["id"]), str)
        self.assertEqual(type(amenity_1_dict["created_at"]), str)
        self.assertEqual(type(amenity_1_dict["updated_at"]), str)

    def test_contrast_to_dict_dunder_dict(self):
        amenity_1 = Amenity()
        self.assertNotEqual(amenity_1.to_dict(), amenity_1.__dict__)

    def test_to_dict_with_None_arg(self):
        amenity_1 = Amenity()
        with self.assertRaises(TypeError):
            amenity_1.to_dict(None)


if __name__ == "__main__":
    unittest.main()
