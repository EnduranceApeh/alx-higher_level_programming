#!/usr/bin/python3
"""
Module 6-base_geometry
This class BaseGeometry raise an exception
"""


class BaseGeometry:
    """Raise an exception
    methods:
        def area(self):
            raise exception

        def integer_validator(self, name, value):
            validates value
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate is value is integer
        Args:
            name: string value
            value: int value
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
