import os
from typing import Dict

import pandas as pd

from forms.base_form import BaseForm

from models.html import NameCountDictHtml, NumerateQuestionSingleAnswerHtml, TextFieldHtml
from .utils import calculate_parameters, processing_info, raw_phases


class Form(BaseForm):
    name = "ost_rusalov"
    display_name = "Опитувальник формально-динамічних властивостей індивідуальності В.М. Русалова"
    path = os.path.dirname(os.path.realpath(__file__)) + "/source.csv"

    def to_html(self):
        return NumerateQuestionSingleAnswerHtml(self.questions).to_html()

    def process_result(self, raw_response: Dict[str, str]) -> str:
        response = {int(key): True if val == "0" else False for key, val in raw_response.items()}
        parameters = calculate_parameters(response)
        body = NameCountDictHtml(parameters, "parameters").to_html()

        body += TextFieldHtml(processing_info, "info").to_html()

        return f"<div class='result ost_rusalov'>{body}</div>"
