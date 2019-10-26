import pytest
from core.math.line_segment import LineSegment
from core.math.vector2 import Vector2


def test_equation():
    l = LineSegment(Vector2(0, 0), Vector2(1, 1))
    assert l.equation() == (1, 0)


def test_equation2():
    l = LineSegment(Vector2(1, 0), Vector2(1, 5))
    assert l.equation() is not None


def test_intersection_img():
    l = LineSegment(Vector2(0, 0), Vector2(.1, .1))
    l2 = LineSegment(Vector2(0, 1), Vector2(1, 0))
    assert l.intersection_point(l2, False) == Vector2(0.5, 0.5)


def test_intersection_real():
    l = LineSegment(Vector2(0, 0), Vector2(1, 1))
    l2 = LineSegment(Vector2(0, 1), Vector2(1, 0))
    assert l.intersection_point(l2, True) == Vector2(0.5, 0.5)


def test_intersection_par():
    l = LineSegment(Vector2(0, 0), Vector2(1, 1))
    l2 = LineSegment(Vector2(1, 1), Vector2(2, 2))
    assert l.intersection_point(l2, True) is None


def test_intersection_real_fase():
    l = LineSegment(Vector2(0, 0), Vector2(100, 100))
    l2 = LineSegment(Vector2(1, 0), Vector2(1, 5))
    assert l.intersection_point(l2, True) is None


def test_intersection_real_par():
    l = LineSegment(Vector2(0, 0), Vector2(100, 100))
    l2 = LineSegment(Vector2(1, 0), Vector2(1, 500))
    assert l.intersection_point(l2, True) is None


def test_compare():
    l = LineSegment(Vector2(0, 0), Vector2(100, 100))
    l2 = LineSegment(Vector2(0, 0), Vector2(100, 100))
    assert l == l2
