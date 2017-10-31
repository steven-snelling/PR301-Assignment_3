from view.i_graph_view import Graph
from plotly import *
import plotly.graph_objs as ob


class SalesByGenderGraph(Graph):

    def __init__(self):
        self.graph_data = None

    def build_graph(self, data_arr):
        gender_data = []
        sales_data = []
        for person in data_arr:
            gender_data.append(person[1])
            sales = int(person[3])
            sales_data.append(sales)
        graph_data = [ob.Bar(
            x=gender_data,
            y=sales_data
        )]
        graph_format = ob.Layout(
            title="Gender Verse Sales Bar Graph",
            xaxis=dict(
                title="Gender"
            ),
            yaxis=dict(
                title="Sales"
            )
        )
        self.graph_data = ob.Figure(data=graph_data, layout=graph_format)

    def show_graph(self):
        offline.plot(self.graph_data)
