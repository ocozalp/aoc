from heapq import heappush, heappop

def solve(items, capacity):
  value, solution, opt = _bfs_bnb(items, capacity)

  taken = [1 if i else 0 for i in solution]
  opt_val = 1 if opt else 0

  output_data = str(value) + ' ' + str(opt_val) + '\n'
  output_data += ' '.join(map(str, taken))
  return output_data

def _bfs_bnb(items, capacity):
  max_heap_size = 300
  sorted_items = sorted(items, key=lambda e: float(e.value)/float(e.weight), reverse=True)
  # print(sorted_items)
  initial_soln = [False]*len(items)
  max_value = _get_max_value(sorted_items, capacity, initial_soln, set())
  print('Initial max value: {}'.format(max_value))

  # value up to that point, previous values, index to evaluate, estimated max val
  frontier = [(-max_value, (0, initial_soln, 0, max_value, capacity, set()))]
  # value, points
  max_solution = (0, [], False)

  items = sorted_items
  while len(frontier) > 0:
    _, elm = heappop(frontier)
    # capacity exceeded
    if elm[4] < 0:
      continue
    if elm[3] < max_solution[0]:
      continue
    # better solution
    if elm[0] > max_solution[0]:
      print ('Max solution changed from {} to {}'.format(max_solution[0], elm[0]))
      max_solution = (elm[0], elm[1], False)
    # current best solution is better than the current max
    if len(elm[5]) == len(items):
      continue

    next_idx = elm[2] + 1
    eval_nodes = elm[5] | {items[elm[2]].index}

    # do not pick the item
    next_max_val = _get_max_value(sorted_items, capacity, elm[1], eval_nodes)
    heappush(frontier, (-next_max_val, (elm[0], elm[1], next_idx, next_max_val, elm[4], eval_nodes)))
    #frontier.insert(0, (elm[0], elm[1], next_idx, next_max_val, elm[4], eval_nodes))

    # pick the item
    sol2 = elm[1][:]
    sol2[items[elm[2]].index] = True
    next_capacity = elm[4] - items[elm[2]].weight
    next_val = elm[0] + items[elm[2]].value
    next_max_val = _get_max_value(sorted_items, capacity, sol2, eval_nodes)
    heappush(frontier, (-next_max_val, (next_val, sol2, next_idx, next_max_val, next_capacity, eval_nodes)))
    #frontier.insert(0, (next_val, sol2, next_idx, next_max_val, next_capacity, eval_nodes))
    if len(frontier) > max_heap_size:
      frontier = frontier[:max_heap_size]

  return max_solution

def _get_max_value(sorted_items, capacity, solution, evaluated_nodes):
  left_capacity = capacity
  max_value = 0
  for i, item in enumerate(sorted_items):
    if item.index in evaluated_nodes and not solution[item.index]:
      continue

    c = 1.0
    if item.weight > left_capacity:
      c = float(left_capacity) / item.weight
    max_value += c * item.value
    left_capacity -= c * item.weight
    if left_capacity <= 0.0:
      break
  return int(max_value)

if __name__ == '__main__':
  from solver import Item
  sorted_items = [Item(index=2, value=35, weight=3), Item(index=0, value=45, weight=5), Item(index=1, value=48, weight=8)]
  capacity = 10
  solution = [True, False, False]
  eval_nodes = {0}
  print(_get_max_value(sorted_items, capacity, solution, eval_nodes))