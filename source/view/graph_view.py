

class GraphView(object):
    def __init__(self, builder):
        self.builder = builder

    def make_graph(self, data_arr):
        self.builder.build_graph(data_arr)
