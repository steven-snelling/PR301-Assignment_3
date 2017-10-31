from view.i_graph_view import Graph
from plotly import *
import plotly.graph_objs as ob


class GraphView(Graph):
    def sales_by_gender_graph(self, data_arr):
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
        graph = ob.Figure(data=graph_data, layout=graph_format)
        self.show_graph(graph)

    def employees_by_gender_graph(self, data_arr):
        male_count = 0
        female_count = 0
        for person in data_arr:
            if person[1] == "M":
                male_count += 1
            if person[1] == "F":
                female_count += 1

        graph_data = {
            'data': [{'labels': ['Male', 'Female'],
                      'values': [male_count, female_count],
                      'type': 'pie'}],
            'layout': {
                'title': 'Number of Employees by Gender'}
        }
        self.show_graph(graph_data)

    def age_verse_salary_graph(self, data_arr):
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

    def bmi_pie_graph(self, data_arr):
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
