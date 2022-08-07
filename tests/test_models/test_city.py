#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_init
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_init(unittest.TestCase):
    """Tests for instantiation of the City class."""

    def test_init_with_no_args(self):
        self.assertEqual(type(City()), City)

    def test_new_instance_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(type(City().id), str)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(type(City().created_at), datetime)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(type(City().updated_at), datetime)

    def test_state_id_is_public_class_str(self):
        city_1 = City()
        self.assertEqual(type(City.state_id), str)
        self.assertIn("state_id", dir(city_1))

    def test_name_is_public_class_str(self):
        city_1 = City()
        self.assertEqual(type(City.name), str)
        self.assertIn("name", dir(city_1))

    def test_two_cities_unique_id(self):
        city_1 = City()
        city_2 = City()
        self.assertNotEqual(city_1.id, city_2.id)

    def test_two_cities_different_created_at(self):
        city_1 = City()
        sleep(0.05)
        city_2 = City()
        self.assertLess(city_1.created_at, city_2.created_at)

    def test_two_cities_different_updated_at(self):
        city_1 = City()
        sleep(0.05)
        city_2 = City()
        self.assertLess(city_1.updated_at, city_2.updated_at)

    def test_str_repr(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        city_1 = City()
        city_1.id = "123456"
        city_1.created_at = city_1.updated_at = dt
        city_1_str = city_1.__str__()
        self.assertIn("[City] (123456)", city_1_str)
        self.assertIn("'id': '123456'", city_1_str)
        self.assertIn("'created_at': " + dt_repr, city_1_str)
        self.assertIn("updated_at': " + dt_repr, city_1_str)

    def test_unused_args(self):
        city_1 = City(None)
        self.assertNotIn(None, city_1.__dict__.values())

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)
