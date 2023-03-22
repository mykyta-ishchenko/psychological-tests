import os
from typing import Dict

from forms.base_form import BaseForm

from models.html import NameCountHtml, NumerateQuestionSingleAnswerHtml, TextFieldHtml
from .utils import calculate_symptoms, processing_info, raw_phases


class Form(BaseForm):
    name = "emotional_burnout_boyko"
    display_name = "Методика діагностики рівня «емоційного вигорання» В.В. Бойка"
    path = os.path.dirname(os.path.realpath(__file__)) + "/source.csv"

    def to_html(self):
        return NumerateQuestionSingleAnswerHtml(self.questions).to_html()

    def process_result(self, raw_response: Dict[str, str]) -> str:
        response = {int(key): True if val == "0" else False for key, val in raw_response.items()}
        symptoms = calculate_symptoms(response)
        phases = {key: sum([symptoms[symptom] for symptom in value]) for key, value in raw_phases.items()}

        body = ""

        for phase, count in phases.items():
            symptoms_generated = ""
            for symptom in raw_phases[phase]:
                symptoms_generated += NameCountHtml(symptom, symptoms[symptom]).to_html()
            body += NameCountHtml(phase, count, symptoms_generated, "phase").to_html()

        body += TextFieldHtml(processing_info, "info").to_html()

        return f"<div class='result emotional_burnout_boyko'>{body}</div>"
