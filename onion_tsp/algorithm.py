from geometry import distance, sq_distance
from graham_scan import graham_scan
from math import sqrt


def tsp(points):
  """
  Calculates the path.
  """
  layers, remaining_points = _get_layers(points)
  if len(layers) == 0:
    return remaining_points

  layers[-1] = _merge(layers[-1], remaining_points)
  while len(layers) > 1:
    l2 = layers.pop()
    l1 = layers.pop()
    l3 = _merge(l1, l2)
    layers.append(l3)

  result = _optimize(layers[0])
  return result, cost(result)


def cost(path):
  """
  Length of the path.
  """
  result = 0
  for i in range(len(path)):
    next_index = (i + 1) % len(path)
    result += distance(path[i], path[next_index])
  return result


def _get_layers(points):
  """
  Returns layers of convex hulls
  """
  layers = []

  remaining_points = points
  while True:
    convex_hull, remaining_points = graham_scan(remaining_points)
    if convex_hull is None:
      break
    layers.append(convex_hull)

  return layers, remaining_points


def _merge(layer1, layer2):
  return _merge_inner_layers(layer1, layer2)


def _merge_inner_layers(layer1, layer2):
  """
  A greedy, cubic merge function.

  This will be used to merge the innermost layer and remaining points. Even the complexity is cubic, the number
  of remaining points is small (actually it's 1 or 2 except extreme cases) so it will not cause any practical problems.
  """
  result = [p for p in layer1]
  points_to_be_added = [p for p in layer2]

  while len(points_to_be_added) > 0:
    min_difference = None
    add_after = -1
    new_point_index = -1
    for i, p1 in enumerate(result):
      next_index = (i + 1) % len(result)
      current_distance = sq_distance(result[i], result[next_index])
      for j, p2 in enumerate(points_to_be_added):
        new_distance = sq_distance(result[i], p2) + sq_distance(p2, result[next_index])
        difference = new_distance - current_distance
        if min_difference is None or difference < min_difference:
          min_difference = difference
          add_after = i
          new_point_index = j

    result = result[:add_after + 1] + [points_to_be_added[new_point_index]] + result[add_after + 1:]
    points_to_be_added.pop(new_point_index)

  return result


def _two_opt(path):
  """
  Another cubic function. Can be optimized.
  """
  found_better = True
  while found_better:
    found_better = False
    for i in range(len(path)):
      for j in range(i + 1, len(path)):
        i_prev_index = (i-1) % len(path)
        j_next_index = (j+1) % len(path)
        if i_prev_index == j:
          break
        # disconnect nodes
        cost_diff = -sq_distance(path[i_prev_index], path[i]) - sq_distance(path[j], path[j_next_index])
        # connect nodes
        cost_diff += sq_distance(path[i], path[j_next_index]) + sq_distance(path[i_prev_index], path[j])

        if cost_diff < 0:
          path = path[:i] + list(reversed(path[i:j + 1])) + path[j + 1:]
          found_better = True
          break
      if found_better:
        break
  return path


def _opt_triangles(path):
  """
  Insert a node between 2 nodes if the new triangle shortens the path.
  """
  found_better = True
  while found_better:
    found_better = False
    for i in range(len(path)):
      for j in range(i + 2, len(path)+1):
        jj = j % len(path)
        next_i = (i + 1) % len(path)
        next_jj = (jj + 1) % len(path)
        prev_jj = (jj - 1 + len(path)) % len(path)

        if jj == next_i or jj == next_i + 1:
          continue

        if next_jj == next_i or next_jj == i or next_jj == next_i + 1:
          continue

        if prev_jj == next_i or prev_jj == i or prev_jj == next_i + i:
          continue

        cost_diff = -sq_distance(path[i], path[next_i]) - sq_distance(path[jj], path[next_jj]) - sq_distance(path[prev_jj], path[jj])
        cost_diff += sq_distance(path[prev_jj], path[next_jj]) + sq_distance(path[i], path[jj]) + sq_distance(path[jj], path[next_i])

        if cost_diff < 0:
          found_better = True
          path = path[:i+1] + [path[jj]] + path[next_i:prev_jj + 1] + path[next_jj:]
          break

      if found_better:
        break
  return path


def _optimize(path):
  """
  Optimizes the final path.
  """
  return _opt_triangles(_two_opt(path))
