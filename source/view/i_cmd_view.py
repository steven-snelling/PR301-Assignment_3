class ICmdView(object):
    def manual_person_flow(self):
        raise NotImplementedError("An abstract method has not been overriden")

    def show(self, show_string):
        raise NotImplementedError("An abstract method has not been overriden")

    def read(self, prompt):
        raise NotImplementedError("An abstract method has not been overriden")
