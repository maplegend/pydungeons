import unittest
from core.math.line_segment import LineSegment
from core.math.vector2 import Vector2
from core.math.rect import Rect


class RectTests(unittest.TestCase):
    def test_intersect_line(self):
        line = LineSegment(Vector2(0, 0), Vector2(10, 10))
        rect = Rect(5, 5, 11, 11)
        self.assertEqual(rect.intersect_point(line), Vector2(5, 5))


if __name__ == '__main__':
    unittest.main()
