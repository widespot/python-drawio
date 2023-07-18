import random
import os
import unittest
from xml.etree.ElementTree import tostring

from python_drawio import Page, Document, RoundedRectangle


class TestRectangle(unittest.TestCase):
    output_dir = "tests/unit/output/test_rectangle/"

    def setUp(self) -> None:
        os.makedirs(TestRectangle.output_dir, exist_ok=True)

    def test_x_y_width_height(self):
        for i in range(100):
            x = random.randint(-1000, 1000)
            y = random.randint(-1000, 1000)
            width = random.randint(1, 1000)
            height = random.randint(1, 1000)

            m = RoundedRectangle(x=x, y=y, width=width, height=height)

            self.assertEqual(m.get_width(), width)
            self.assertEqual(m.get_height(), height)

    def test_exception_width_height(self):
        with self.assertRaises(AssertionError):
            RoundedRectangle(x=1, y=1, width=1, height=0)
        with self.assertRaises(AssertionError):
            RoundedRectangle(x=1, y=1, width=0, height=1)
        with self.assertRaises(AssertionError):
            # noinspection PyTypeChecker
            RoundedRectangle(x=1, y=1, width=0.1, height=1)
        with self.assertRaises(AssertionError):
            # noinspection PyTypeChecker
            RoundedRectangle(x=1, y=1, width=1, height=0.1)
        with self.assertRaises(AssertionError):
            RoundedRectangle(x=1, y=1, width=1, height=-1)
        with self.assertRaises(AssertionError):
            RoundedRectangle(x=1, y=1, width=-1, height=1)
        with self.assertRaises(AssertionError):
            # noinspection PyTypeChecker
            RoundedRectangle(x=1, y=1, width=1, height="1")
        with self.assertRaises(AssertionError):
            # noinspection PyTypeChecker
            RoundedRectangle(x=1, y=1, width="1", height=1)
        with self.assertRaises(TypeError):
            # noinspection PyArgumentList
            RoundedRectangle(x=1, y=1, width=1)
        with self.assertRaises(TypeError):
            # noinspection PyArgumentList
            RoundedRectangle(x=1, y=1, height=1)
