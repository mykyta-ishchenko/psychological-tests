from typing import Dict

from forms.base_form import BaseForm
from forms.models import AnswerType, ProcessingTF
from forms.utils import connect_to_upper_group

from .utils import group_level_1, parameters as dict_params


class Form(BaseForm):
    name = "Yatsenko_childrens_temperament_type"
    display_name = "Методика визначення типу темпераменту дитини (Т.В. Яценко)"
    type = AnswerType.tf

    def process_result(self, raw_response: Dict[str, str]) -> Dict:
        return connect_to_upper_group(
            upper_group=group_level_1,
            func=sum,
            params=ProcessingTF(dict_params, raw_response).process(),
        )
