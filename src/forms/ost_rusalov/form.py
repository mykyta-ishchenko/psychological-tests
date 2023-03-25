import os
from typing import Dict

import pandas as pd

from forms.base_form import BaseForm

from .utils import calculate_parameters

from forms.models import AnswerType

from markdown import markdown


class Form(BaseForm):
    name = "ost_rusalov"
    display_name = "Опитувальник формально-динамічних властивостей індивідуальності В.М. Русалова"
    path = os.path.dirname(os.path.realpath(__file__)) + "/source.csv"
    type = AnswerType.tf
    processing_info = markdown(open(os.path.dirname(os.path.realpath(__file__)) + "/processing.md").read())

    def process_result(self, raw_response: Dict[str, str]) -> Dict:
        response = {int(key): True if val == "true" else False for key, val in raw_response.items()}
        parameters = calculate_parameters(response)
        parameters = {key: (val,) for key, val in parameters.items()}
        return parameters
