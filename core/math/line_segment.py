from .vector2 import Vector2


class LineSegment:
    def __init__(self, start, end):
        '''
        :param start: start point
        :param end: end point
        '''
        self.start = start
        self.end = end

    def vector(self):
        return self.end - self.start

    def equation(self):
        # Returns k and b from y = kx + b
        vec = self.vector()
        k = vec.y/(vec.x if vec.x != 0 else 0.000001)
        return k, self.start.y - self.start.x*k

    def intersection_point(self, line, real=True):
        '''
        :param line: second line
        :param real: if true and point of intersection does not lay on both line segments method will return None
        :return: point of intersection
        '''
        e = 0.001
        eq = self.equation()
        seq = line.equation()
        if -e <= eq[0] - seq[0] <= e:
            return None

        x = (seq[1] - eq[1]) / (eq[0] - seq[0])
        y = eq[0]*x + eq[1]
        if real:
            def lay_on_line(l):
                return min(l.start.x, l.end.x) <= x <= max(l.start.x, l.end.x) \
                          and min(l.start.y, l.end.y) <= y <= max(l.start.y, l.end.y)
            if not lay_on_line(self) or not lay_on_line(line):
                return None

        return Vector2(x, y)
