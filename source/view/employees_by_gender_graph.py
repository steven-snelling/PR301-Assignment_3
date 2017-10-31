from view.i_graph_view import Graph
from plotly import *
import plotly.graph_objs as ob


class EmployeesByGenderGraph(Graph):

    def __init__(self):
        self.graph_data = None

    def build_graph(self, data_arr):
        male_count = 0
        female_count = 0
        for person in data_arr:
            if person[1] == "M":
                male_count += 1
            if person[1] == "F":
                female_count += 1

        self.graph_data = {
            'data': [{'labels': ['Male', 'Female'],
                      'values': [male_count, female_count],
                      'type': 'pie'}],
            'layout': {
                'title': 'Number of Employees by Gender'}
        }

    def show_graph(self):
        offline.plot(self.graph_data)
