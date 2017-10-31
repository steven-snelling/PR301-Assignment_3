from view.i_graph_view import Graph
from plotly import *
import plotly.graph_objs as ob


class AgeVerseSalaryGraph(Graph):

    def __init__(self):
        self.graph_data = None

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
        self.graph_data = ob.Figure(data=graph_data, layout=graph_format)

    def show_graph(self):
        offline.plot(self.graph_data)
