class Timeline(object):

    def __init__(self, max_value):
        self.max_value = max_value

    def get(self, index):
        raise NotImplementedError("Not implemented!")

    def inc(self, start, end, d):
        raise NotImplementedError("Not implemented!")


class SimpleTimeline(Timeline):

    def __init__(self, max_value):
        super(SimpleTimeline, self).__init__(max_value)
        self.data = [0] * (max_value+1)

    def get(self, index):
        return self.data[index]

    def inc(self, start, end, d):
        if not 0 <= start <= end <= self.max_value:
            raise Exception("Invalid index! %d - %d (max: %d)" % (start, end, self.max_value))

        for i in xrange(start, end + 1):
            self.data[i] += 1
