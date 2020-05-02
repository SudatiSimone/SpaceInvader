from unittest import TestCase

from main import isCollision


class TestIsCollision1(TestCase):
    def test_isCollision1(self):
        self.assertFalse(isCollision(23, 2, 2, 20))


class TestIsCollision2(TestCase):
    def test_isCollision2(self):
        self.assertTrue(isCollision(18, 2, 3, 20))


