import argparse
import matplotlib.pyplot as plt

from algorithm import tsp
from cli import parse_arguments, get_points, plot_graph


def main():
  args = parse_arguments('Orhan\'s TSP solver')
  points = get_points(args)

  verbose = args.verbose

  result, cost = tsp(points)
  if verbose:
    print('Result: {}'.format(result))
  print('Cost: {}'.format(cost))

  if args.plot:
    plot_graph(result)


if __name__ == '__main__':
  main()
