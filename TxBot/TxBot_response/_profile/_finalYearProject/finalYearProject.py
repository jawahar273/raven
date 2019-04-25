
from TxBot_response.abstract_response import TxBaseResponse


class FinalYearProject(TxBaseResponse):

    def __init__(self):
        super(FinalYearProject, self).__init__(self)

    def get_class_name(self):
        return self.__class__.__name__

    def render(self):
        self.class_name = self.get_class_name()  # class name

        super().render(class_name=self.class_name, sub_path='_profile')

        return self.render_template.render()

