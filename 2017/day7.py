class Node:

    def __init__(self, weight):
        self.weight = weight
        self.total_weight = weight
        self.children = list()


class Tree:

    def __init__(self):
        self.root = None
        self.nodes = dict()

    def add_node(self, name, weight):
        node = Node(weight)
        self.nodes[name] = node

    def connect(self, src, destination):
        self.nodes[src].children.append(destination)


def create_tree(lines):
    tree = Tree()
    for line in lines:
        weight = int(line[1][1:-1])
        tree.add_node(line[0], weight)

        if len(line) > 2:
            for child in line[3:]:
                c = child
                if c[-1] == ',':
                    c = c[:-1]
                tree.connect(line[0], c)
    return tree


def part1(tree):
    incoming = {node: 0 for node in tree.nodes}

    for node in tree.nodes:
        for c in tree.nodes[node].children:
            incoming[c] += 1

    root = None
    for k in incoming:
        if incoming[k] == 0:
            root = k

    tree.root = tree.nodes[root]
    return root


def weight_increment(tree, node):
    weights = [weight_increment(tree, tree.nodes[c]) for c in node.children]
    node.total_weight += sum(weights)

    return node.total_weight


def balance(tree, node, target_val):
    if len(node.children) <= 1:
        return 0

    weights = [(tree.nodes[c].total_weight, c) for c in node.children]
    weights.sort()

    if weights[-1][0] == weights[0][0]:
        return abs(target_val - node.total_weight + node.weight)

    if weights[1][0] == weights[0][0]:
        return balance(tree, tree.nodes[weights[-1][1]], weights[0][0])

    return balance(tree, tree.nodes[weights[0][1]], weights[-1][0])


def part2(tree):
    weight_increment(tree, tree.root)
    return balance(tree, tree.root, tree.root.total_weight)


def main():
    with open('input/day7.txt', 'r') as f:
        lines = map(lambda s: s.split(), map(lambda l: l[:-1], f.readlines()))

    tree = create_tree(lines)

    print 'Part 1: ', part1(tree)
    print 'Part 2: ', part2(tree)


if __name__ == '__main__':
    main()