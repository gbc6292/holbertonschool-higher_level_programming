import unittest
""" In this module are defined the BaseClass"""


class Base(unittest.TestCase):
    """This is a BaseClass"""
    __nb_objects = 0

    def test__init__(self, id=None):
        """Defining the attributes and methods
        of the BaseClass"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


if __name__ == '__main__':
    unittest.main()
