#!/usr/bin/python3

import unittest
from models import base
Base = base.Base
class BaseTest(unittest.TestCase):
    """Run this test with python3 -m tests.base"""

    def test_id_given(self):
        """Test if id given matches"""

        self.assertEqual(Base(123),  self.id)



if __name__ == "__main__":
    unittest.main()

