#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview_init
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_init(unittest.TestCase):
    """Tests testing instantiation of Review class."""

    def test_init_with_no_args(self):
        self.assertEqual(type(Review()), Review)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(type(Review().id), str)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(type(Review().created_at), datetime)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(type(Review().updated_at), datetime)

    def test_place_id_is_public_class_str(self):
        review_1 = Review()
        self.assertEqual(type(Review.place_id), str)
        self.assertIn("place_id", dir(review_1))

    def test_user_id_is_public_class_str(self):
        review_1 = Review()
        self.assertEqual(type(Review.user_id), str)
        self.assertIn("user_id", dir(review_1))

    def test_text_is_public_class_str(self):
        review_1 = Review()
        self.assertEqual(type(Review.text), str)
        self.assertIn("text", dir(review_1))

    def test_two_reviews_unique_ids(self):
        review_1 = Review()
        review_2 = Review()
        self.assertNotEqual(review_1.id, review_2.id)

    def test_two_reviews_different_created_at(self):
        review_1 = Review()
        sleep(0.05)
        review_2 = Review()
        self.assertLess(review_1.created_at, review_2.created_at)

    def test_two_reviews_different_updated_at(self):
        review_1 = Review()
        sleep(0.05)
        review_2 = Review()
        self.assertLess(review_1.updated_at, review_2.updated_at)

    def test_str_repr(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        review_1 = Review()
        review_1.id = "123456"
        review_1.created_at = review_1.updated_at = dt
        review_1_str = review_1.__str__()
        self.assertIn("[Review] (123456)", review_1_str)
        self.assertIn("'id': '123456'", review_1_str)
        self.assertIn("'created_at': " + dt_repr, review_1_str)
        self.assertIn("'updated_at': " + dt_repr, review_1_str)

    def test_unused_args(self):
        review_1 = Review(None)
        self.assertNotIn(None, review_1.__dict__.values())

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """Tests for save method of the class."""

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
        review_1 = Review()
        sleep(0.05)
        prior_updated_at = review_1.updated_at
        review_1.save()
        self.assertLess(prior_updated_at, review_1.updated_at)

    def test_save_with_None_arg(self):
        review_1 = Review()
        with self.assertRaises(TypeError):
            review_1.save(None)

    def test_save_updates_file_with_review(self):
        review_1 = Review()
        review_1.save()
        review_1_id = "Review." + review_1.id
        with open("file.json", "r") as f:
            self.assertIn(review_1_id, f.read())


class TestReview_to_dict(unittest.TestCase):
    """Tests for to_dict method of the class."""

    def test_to_dict_type(self):
        self.assertEqual(type(Review().to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        review_1 = Review()
        self.assertIn("id", review_1.to_dict())
        self.assertIn("created_at", review_1.to_dict())
        self.assertIn("updated_at", review_1.to_dict())
        self.assertIn("__class__", review_1.to_dict())

    def test_to_dict_contains_added_attrs(self):
        review_1 = Review()
        review_1.pet_name = "Dan"
        review_1.phone = 123456
        self.assertEqual(review_1.pet_name, "Dan")
        self.assertIn("phone", review_1.to_dict())

    def test_to_dict_datetime_attrs_are_str(self):
        review_1 = Review()
        review_1_dict = review_1.to_dict()
        self.assertEqual(type(review_1_dict["created_at"]), str)
        self.assertEqual(type(review_1_dict["updated_at"]), str)

    def test_contrast_to_dict_dunder_dict(self):
        review_1 = Review()
        self.assertNotEqual(review_1.to_dict(), review_1.__dict__)

    def test_to_dict_with_None_arg(self):
        review_1 = Review()
        with self.assertRaises(TypeError):
            review_1.to_dict(None)


if __name__ == "__main__":
    unittest.main()
