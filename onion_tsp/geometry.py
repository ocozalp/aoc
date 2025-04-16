import math

def dot_product(p, q, r):
  """
  Dot product of two vectors, p->q and q->r.
  """
  return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])


def sq_distance(p, q):
  """
  Square of Euclidean distance between 2 points.
  """
  return (p[1]-q[1]) ** 2 + (p[0]-q[0]) ** 2


def distance(p, q):
  """
  Square of Euclidean distance between 2 points.
  """
  return math.sqrt((p[1]-q[1]) ** 2 + (p[0]-q[0]) ** 2)