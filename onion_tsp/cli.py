import argparse

from geometry import distance


def parse_arguments(description):
  parser = argparse.ArgumentParser(description=description)
  parser.add_argument('--height', dest='height', type=int, help='Height of the map', required=True)
  parser.add_argument('--width', dest='width', type=int, help='Width of the map', required=True)
  parser.add_argument('-n', dest='number_of_points', type=int, help='Number of points', required=True)
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-r', dest='is_random', help='Generate random points.', action='store_true')
  group.add_argument('-f', dest='from_file', help='Read from file.', action='store_true')
  parser.add_argument('-p', dest='plot', help='Plot graph.', action='store_true')
  parser.add_argument('-v', dest='verbose', help='Verbose.', action='store_true')

  return parser.parse_args()


def get_points(args):
  height = args.height
  width = args.width
  number_of_points = args.number_of_points
  verbose = args.verbose

  if args.is_random:
    points = generate_random_points(width, height, number_of_points)
  elif args.from_file:
    points = read_points_from_file(width, height, number_of_points)
  else:
    print('Should not have happened')
    exit(1)

  if verbose:
    print('Input Points: {}'.format(points))

  return points


def generate_random_points(max_x, max_y, number_of_points):
  import random

  points = set()
  while len(points) < number_of_points:
    points.add((random.randint(0, max_x), random.randint(0, max_y)))
  return list(points)


def read_points_from_file(max_x, max_y, number_of_points):
  import json
  from os.path import exists, dirname, abspath

  directory = dirname(abspath(__file__))
  file_name = '{}/maps/{}x{}_{}.json'.format(directory, max_x, max_y, number_of_points)
  if not exists(file_name):
    print('File ({}) does not exist. Quitting...'.format(file_name))
    exit(1)

  with open(file_name, 'r') as f:
    return json.load(f)['points']


def plot_graph(result):
  import matplotlib.pyplot as plt

  x = list(map(lambda p: p[0], result)) + [result[0][0]]
  y = list(map(lambda p: p[1], result)) + [result[0][1]]
  plt.plot(x, y, 'r')
  plt.plot(x, y, 'ro')
  plt.plot([x[0]], [y[0]], 'bo')

  for i, (_x, _y) in enumerate(zip(x[:-1], y[:-1])):
    lbl = '[{}]({}, {})'.format(i, _x, _y)
    plt.annotate(lbl, (_x, _y), textcoords='offset points', xytext=(0, 5), ha='center')
    next_i = (i+1)%len(x)
    _x1 = x[next_i]
    _y1 = y[next_i]
    lbl = '{}'.format(distance((_x, _y), (_x1, _y1)))
    plt.annotate(lbl, ((_x+_x1)//2, (_y+_y1)//2), textcoords='offset points', xytext=(0, 5), ha='center')
  plt.show()
