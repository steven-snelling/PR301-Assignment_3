from view.i_graph_view import Graph
from plotly import *


class BmiPieGraph(Graph):

    def build_graph(self, data_arr):
        normal_count = 0
        obesity_count = 0
        underweight_count = 0
        overweight_count = 0
        for person in data_arr:
            if person[4] == "Normal":
                normal_count += 1
            if person[4] == "Overweight":
                overweight_count += 1
            if person[4] == "Obesity":
                obesity_count += 1
            if person[4] == "Underweight":
                underweight_count += 1
        graph_data = {
            'data': [{'labels': ['Normal', 'Overweight', 'Obesity',
                                 'Underweight'],
                      'values': [normal_count, overweight_count,
                                 obesity_count, underweight_count],
                      'type': 'pie'}],
            'layout': {
                'title': 'Staff by BMI'}
        }
        self.show_graph(graph_data)

    @staticmethod
    def show_graph(graph_data):
        offline.plot(graph_data)
