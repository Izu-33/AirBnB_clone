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
