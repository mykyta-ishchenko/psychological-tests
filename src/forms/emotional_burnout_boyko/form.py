import os
from typing import Dict

from forms.base_form import BaseForm

from .utils import calculate_params, group_level_1, connect_to_upper_group

from forms.models import AnswerType

from markdown import markdown


class Form(BaseForm):
    name = "emotional_burnout_boyko"
    display_name = "Методика діагностики рівня «емоційного вигорання» В.В. Бойка"
    path = os.path.dirname(os.path.realpath(__file__)) + "/source.csv"
    type = AnswerType.tf
    processing_info = markdown(open(os.path.dirname(os.path.realpath(__file__)) + "/processing.md").read())

    def process_result(self, raw_response: Dict[str, str]) -> Dict:
        print(raw_response)
        response = {int(key): True if val == "true" else False for key, val in raw_response.items()}
        params = calculate_params(response)
        processed_groups = {key: sum([params[param] for param in value]) for key, value in group_level_1.items()}
        return connect_to_upper_group(processed_groups, group_level_1, params)
