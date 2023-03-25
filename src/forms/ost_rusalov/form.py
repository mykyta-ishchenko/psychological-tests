from typing import Dict

from forms.base_form import BaseForm
from forms.models import AnswerType, ProcessingTF

from .utils import parameters as params_dict


class Form(BaseForm):
    name = "ost_rusalov"
    display_name = "Опитувальник формально-динамічних властивостей індивідуальності В.М. Русалова"
    type = AnswerType.tf

    def process_result(self, raw_response: Dict[str, str]) -> Dict:
        return ProcessingTF(params_dict, raw_response).process()
