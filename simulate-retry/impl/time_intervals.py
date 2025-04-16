from impl.timeline import Timeline


class TimeIntervals(Timeline):

    class Node:
        def __init__(self, start, end, val):
            self.start = start
            self.end = end
            self.val = val
            self.next_node = None

    def __init__(self, max_value):
        super(TimeIntervals, self).__init__(max_value)
        self.head = TimeIntervals.Node(1, max_value, 0)

    def get(self, index):
        if index > self.max_value or 0 > index:
            raise Exception('Index (%d) out of bounds' % index)

        current = self.head
        while current is not None:
            if current.start <= index <= current.end:
                return current.val
            current = current.next_node

        raise Exception('Unexpected state in get()')

    def inc(self, start, end, d):
        parent = None
        current = self.head
        current_start = start
        while current is not None:
            next_node = current.next_node

            if current.end >= current_start:
                new_nodes = self.__divide_node(current, current_start, end, d)

                if parent is not None:
                    if parent.val != new_nodes[0].val:
                        parent.next_node = new_nodes[0]
                    else:
                        parent.end = new_nodes[0].end
                        new_nodes[0] = parent
                        if len(new_nodes) > 1:
                            parent.next_node = new_nodes[1]
                else:
                    self.head = new_nodes[0]

                if len(new_nodes) == 2 and next_node is not None and new_nodes[1].val == next_node.val:
                    new_nodes[1].end = next_node.end
                    # wtf
                    next_node = next_node.next_node
                    new_nodes[1].next_node = next_node
                else:
                    new_nodes[-1].next_node = next_node

                current = new_nodes[-1]
                current_start = current.end + 1
            elif current.start > end:
                break

            parent = current
            current = next_node

    def __divide_node(self, node, start, end, d):
        result = list()
        if start > node.start:
            result.append(TimeIntervals.Node(node.start, start - 1, node.val))

        result.append(TimeIntervals.Node(start, min(end, node.end), node.val + d))

        if end < node.end:
            result.append(TimeIntervals.Node(end + 1, node.end, node.val))

        for i in xrange(1, len(result)):
            result[i-1].next_node = result[i]

        return result
