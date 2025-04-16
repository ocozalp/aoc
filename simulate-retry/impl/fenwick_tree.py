from impl.timeline import Timeline


class FenwickTree(Timeline):

    def __init__(self, max_value):
        super(FenwickTree, self).__init__(max_value)
        self.data = [0] * (max_value + 1)

    def get(self, index):
        current_index = index
        result = 0
        while current_index > 0:
            result += self.data[current_index]
            rightmost = current_index & (-current_index)
            current_index -= rightmost
        return result

    def inc(self, start, end, d):
        self.add(start, d)
        self.add(end + 1, -d)

    def add(self, index, d):
        current_index = index
        while current_index <= self.max_value:
            self.data[current_index] += d
            rightmost = current_index & (-current_index)
            current_index += rightmost
