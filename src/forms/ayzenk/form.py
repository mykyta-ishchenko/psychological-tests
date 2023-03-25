from typing import Dict

from forms.base_form import BaseForm
from forms.models import AnswerType, ProcessingTF
from forms.utils import connect_to_upper_group

from .utils import parameters as dict_params


class Form(BaseForm):
    name = "ayzenk"
    display_name = "Опитувальник Г. Айзенка"
    type = AnswerType.tf

    def process_result(self, raw_response: Dict[str, str]) -> Dict:
        return ProcessingTF(dict_params, raw_response).process()
