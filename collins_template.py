class CollinsSpan:

    def __init__(self, i, j, h, score):
        self.i = i
        self.j = j
        self.h = h
        self.score = score

    def __str__(self):
        return "[%s, %s, %s, %s]" % (self.i, self.j, self.h, self.score)

class CollinsParser:

    def __init__(self):
        self.chart = None

    def parse(self, words):
        None

    def init_spans(self, words):
        None

    def add_span(self, new_span):
        None

    def get_score(self, words, head, dep):
        None

    """ Find the highest-scored span [i, j] """
    def find_best(self, i, j):
        None
