from view.i_graph_view import Graph
from plotly import *
import plotly.graph_objs as ob


class AgeVerseSalaryGraph(Graph):

    def build_graph(self, data_arr):
        age_data = []
        salary_data = []
        for person in data_arr:
            age_data.append(person[2])
            salary = int(person[5]) * 1000
            salary_data.append(salary)
        graph_data = [ob.Scatter(
            x=age_data,
            y=salary_data,
            marker=dict(
                color="rgb(16, 32, 77)"
            ),
            name="Age Verse Salary"
        )]
        graph_format = ob.Layout(
            title="Salary Verse Age Scatter Graph",
            xaxis=dict(
                title="Age"
            ),
            yaxis=dict(
                title="Salary"
            )
        )
        graph = ob.Figure(data=graph_data, layout=graph_format)
        self.show_graph(graph)

    @staticmethod
    def show_graph(graph_data):
        offline.plot(graph_data)
