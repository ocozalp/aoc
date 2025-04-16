import math
from functools import cmp_to_key

from geometry import dot_product, sq_distance

def graham_scan(points):
  """
  Calculates a convex hull from a list of 2D points using the Graham Scan Algorithm.
  Returns the convex hull and the remaning points. If the point set does not contain a convex hull, it returns None as
  the convex hull and the input points as the remaining points.
  """
  if len(points) < 3:
    return None, points

  bottom_left = _get_bottom_left(points)
  remaining_points = list(filter(lambda e: e != bottom_left, points))
  remaining_points =  sorted(remaining_points, key=cmp_to_key(_get_comparator(bottom_left)))

  result = [bottom_left, remaining_points[0]]
  points_inside = []

  for r in remaining_points[1:]:
    p, q = result[-2:]
    while _is_right_turn(p, q, r):
      points_inside.append(result.pop())
      if len(result) == 1:
        break
      p, q = result[-2:]
    result.append(r)

  if len(result) < 3:
    return None, points

  return result, points_inside

def _is_right_turn(p, q, r):
  """
  Returns true if p->q->r is a right turn.
  """
  return dot_product(p, q, r) > 0

def _get_bottom_left(points):
  """
  Sort by y-axis and x-axis respectively.
  """
  return min(points, key=lambda p: (p[1], p[0]))

def _get_comparator(pivot_point):
  """
  Returns the comparator function to be used when sorting the remaining points.
  """
  def f(q, r):
    """
    If the dot product of pivot_point->q (v1) and q->r (v2) is not zero, then return that value. A negative dot product
    means the angle between x-axis and v1 is smaller than the one between x-axis and v2 so it's a better candidate
    for a convex hull. If the value is zero that means these 3 points are on the same line. In this case, q and r are
    compared by their distances to pivot_point.
    """
    return dot_product(pivot_point, q, r) or sq_distance(pivot_point, q) - sq_distance(pivot_point, r)
  return f
