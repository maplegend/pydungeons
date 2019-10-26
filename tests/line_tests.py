import unittest
from core.math.line_segment import LineSegment
from core.math.vector2 import Vector2


class LineTest(unittest.TestCase):
    def test_equation(self):
        l = LineSegment(Vector2(0, 0), Vector2(1, 1))
        self.assertEqual(l.equation(), (1, 0))

    def test_equation2(self):
        l = LineSegment(Vector2(1, 0), Vector2(1, 5))
        self.assertNotEqual(l.equation(), None)

    def test_intersection_img(self):
        l = LineSegment(Vector2(0, 0), Vector2(.1, .1))
        l2 = LineSegment(Vector2(0, 1), Vector2(1, 0))
        self.assertEqual(l.intersection_point(l2, False), Vector2(0.5, 0.5))

    def test_intersection_real(self):
        l = LineSegment(Vector2(0, 0), Vector2(1, 1))
        l2 = LineSegment(Vector2(0, 1), Vector2(1, 0))
        self.assertEqual(l.intersection_point(l2, True), Vector2(0.5, 0.5))

    def test_intersection_par(self):
        l = LineSegment(Vector2(0, 0), Vector2(1, 1))
        l2 = LineSegment(Vector2(1, 1), Vector2(2, 2))
        self.assertEqual(l.intersection_point(l2, True), None)

    def test_intersection_real_fase(self):
        l = LineSegment(Vector2(0, 0), Vector2(100, 100))
        l2 = LineSegment(Vector2(1, 0), Vector2(1, 5))
        self.assertEqual(l.intersection_point(l2, True), None)

    def test_intersection_real_par(self):
        l = LineSegment(Vector2(0, 0), Vector2(100, 100))
        l2 = LineSegment(Vector2(1, 0), Vector2(1, 500))
        self.assertEqual(l.intersection_point(l2, True), None)


if __name__ == '__main__':
    unittest.main()
