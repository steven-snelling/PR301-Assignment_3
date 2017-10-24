
class IGraphView(object):
    def sales_by_gender_graph(self, data_arr):
        raise NotImplementedError("An abstract method has not been overriden")

    def employees_by_gender_graph(self, data_arr):
        raise NotImplementedError("An abstract method has not been overriden")

    def age_verse_salary_graph(self, data_arr):
        raise NotImplementedError("An abstract method has not been overriden")

    def bmi_pie_graph(self, data_arr):
        raise NotImplementedError("An abstract method has not been overriden")
