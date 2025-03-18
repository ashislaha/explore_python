
import sys
import os
import unittest
from geometry.Point import Point

# Get the absolute path of the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class TestPoint(unittest.TestCase):
    
    def test_point(self):
        point = Point(10, 10)
        anotherPoint = Point(5,5)
        self.assertNotEqual(point, anotherPoint)

if __name__ == "__main__":
    unittest.main()