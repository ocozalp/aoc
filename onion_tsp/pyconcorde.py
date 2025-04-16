from cli import parse_arguments, get_points, plot_graph
from concorde.tsp import TSPSolver


def solve(points, verbose):
  xs = [p[0] for p in points]
  ys = [p[1] for p in points]
  solver = TSPSolver.from_data(xs, ys, 'EUC_2D')
  solution = solver.solve(verbose=verbose)

  path = _generate_path_from_solution(solution, points)
  return path, solution.optimal_value


def main():
  args = parse_arguments('Wrapper for PyConcorde.')
  points = get_points(args)

  result, cost = solve(points, args.verbose)
  print('Concorde result: {}'.format(result))
  print('Cost: {}'.format(cost))

  if args.plot:
    plot_graph(result)


def _generate_path_from_solution(solution, points):
  result = list()
  for idx in solution.tour:
    result.append(points[idx])
  return result


if __name__ == '__main__':
  main()
