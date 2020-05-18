# Python implementation of Skiena's Programming Challenges

# Chapter 13: Geometry

import math
import sys

EPSILON = sys.float_info.epsilon


class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.x, self.y))

class Line:
    def __init__(self, a=None, b=None, c=None):
        # ax + by + c = 0
        # with b always == 1 when b != 0
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return repr((self.a, self.b, self.c))

def points_to_line(p1, p2):
    # return the Line formed by Points p1 and p2
    l = Line()
    if p1.x == p2.x:
        # vertical line
        l.a, l.b, l.c = 1, 0, -p1.x
    else:
        l.a = - (p1.y - p2.y) / (p1.x - p2.x)
        l.b = 1
        l.c = - (l.a * p1.x) - (l.b * p1.y)
    return l

def point_and_slope_to_line(point, slope):
    # return the Line with given slope containing point
    a, b = -m, 1
    c = - (a * point.x) - (b * point.y)
    return Line(a, b, c)

def parallel(l1, l2):
    # whether l1 // l2
    # it is the case if they have the same slope
    return (math.isclose(l1.a, l2.a) and math.isclose(l1.b, l2.b))

def same_line(l1, l2):
    # whether l1 == l2
    # in addition to being parallel, have same intercept
    return (parallel(l1, l2) and math.isclose(l1.c, l2.c))

def intersection_point(l1, l2):
    if same_line (l1, l2):
        print("Warning: Identical lines, all points intersect.")
        return (Point(0.0,0.0))

    if parallel(l1, l2):
        print("Error: Distinct parallel lines do not intersect.")
        return None

    x = (l2.b*l1.c - l1.b*l2.c) / (l2.a*l1.b - l1.a*l2.b)

    if math.fabs(l1.b) > EPSILON: # tests for vertical line
        y = - (l1.a*x + l1.c) / l1.b
    else:
        y = - (l2.a*x + l2.c) / l2.b

    return Point(x, y)


def closest_point(p, l):
    # return the closest point to p on l

    if math.fabs(l1.b) <= EPSILON:
        # vertical line
        x = - l1.c
        y = p.y
        return Point(x,y)

    if math.fabs(l1.a) <= EPSILON:
        # horizontal line
        x = p.x
        y = - l1.c
        return Point(x,y)

    else:
        # Normal case: it's the intersection of the line through p
        # perpendicular to l
        perpl = point_and_slope_to_line(p, 1.0/l.a)
        return intersection_point(l, perpl)


def signed_triangle_area(a: Point, b: Point, c: Point):
    return ( a.x*b.y - a.x*c.y - b.x*a.y + b.x*c.y + c.x*a.y - c.x*b.y )

def triangle_area(a: Point, b: Point, c:Point):
    return math.fabs(signed_triangle_area(a, b, c))
