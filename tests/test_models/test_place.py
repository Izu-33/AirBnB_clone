#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_init
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_init(unittest.TestCase):
    """Tests for instantiation of Place class."""

    def test_init_with_no_args(self):
        self.assertEqual(type(Place()), Place)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(type(Place().id), str)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(type(Place().created_at), datetime)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(type(Place().updated_at), datetime)

    def test_city_id_is_public_class_attr(self):
        place_1 = Place()
        self.assertEqual(type(Place.city_id), str)
        self.assertIn("city_id", dir(place_1))

    def test_user_id_is_public_class_attr(self):
        place_1 = Place()
        self.assertEqual(type(Place.user_id), str)
        self.assertIn("user_id", dir(place_1))

    def test_name_is_public_class_attr(self):
        place_1 = Place()
        self.assertEqual(type(Place.name), str)
        self.assertIn("name", dir(place_1))

    def test_description_is_public_class_attr(self):
        place_1 = Place()
        self.assertEqual(type(Place.description), str)
        self.assertIn("description", dir(place_1))

    def test_number_rooms_is_public_class_attr(self):
        place_1 = Place()
        self.assertEqual(type(Place.number_rooms), int)
        self.assertIn("number_rooms", dir(place_1))

    def test_number_bathrooms_is_public_class_attr(self):
        place_1 = Place()
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertIn("number_bathrooms", dir(place_1))

    def test_max_guest_is_public_class_attr(self):
        place_1 = Place()
        self.assertEqual(type(Place.max_guest), int)
        self.assertIn("max_guest", dir(place_1))

    def test_price_by_night_is_public_class_attr(self):
        place_1 = Place()
        self.assertEqual(type(Place.price_by_night), int)
        self.assertIn("price_by_night", dir(place_1))

    def test_latitude_is_public_class_attr(self):
        place_1 = Place()
        self.assertEqual(type(Place.latitude), float)
        self.assertIn("latitude", dir(place_1))

    def test_longitude_is_public_class_attr(self):
        place_1 = Place()
        self.assertEqual(type(Place.longitude), float)
        self.assertIn("longitude", dir(place_1))

    def test_amenity_ids_is_public_attr(self):
        place_1 = Place()
        self.assertEqual(type(Place.amenity_ids), list)
        self.assertIn("amenity_ids", dir(place_1))

    def test_two_places_unique_ids(self):
        place_1 = Place()
        place_2 = Place()
        self.assertNotEqual(place_1.id, place_2.id)

    def test_two_places_different_created_at(self):
        place_1 = Place()
        sleep(0.05)
        place_2 = Place()
        self.assertLess(place_1.created_at, place_2.created_at)

    def test_two_places_different_updated_at(self):
        place_1 = Place()
        sleep(0.05)
        place_2 = Place()
        self.assertLess(place_1.updated_at, place_2.updated_at)

    def test_str_repr(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        place_1 = Place()
        place_1.id = "123456"
        place_1.created_at = place_1.updated_at = dt
        place_1_str = place_1.__str__()
        self.assertIn("[Place] (123456)", place_1_str)
        self.assertIn("'id': '123456'", place_1_str)
        self.assertIn("'created_at': " + dt_repr, place_1_str)
        self.assertIn("'updated_at': " + dt_repr, place_1_str)

    def test_unused_args(self):
        place_1 = Place(None)
        self.assertNotIn(None, place_1.__dict__.values())

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)
