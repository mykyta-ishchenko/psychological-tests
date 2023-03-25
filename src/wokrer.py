from forms.base_form import BaseForm


class Worker:
    def __init__(self, *forms: BaseForm):
        self.forms = list(forms)
        self.forms.sort(key=lambda f: f.display_name)

    def get(self, name: str) -> BaseForm | None:
        for form in self.forms:
            if form.name == name:
                return form
        return None
