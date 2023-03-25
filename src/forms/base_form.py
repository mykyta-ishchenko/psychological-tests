import os
from typing import Dict

import markdown
import pandas as pd

from .models import AnswerType, Question


class BaseForm:
    name = "base"
    display_name = "Base Test Form"
    questions = []
    type = AnswerType.choice
    source_path = "data/source.csv"
    info_path = "data/processing.md"

    def __init__(self):
        if self.source_path:
            self.load()

    def load(self) -> None:
        self.questions = []
        df = pd.read_csv(self.base_path + self.source_path)
        for index, row in df.iterrows():
            answers = []

            match self.type:
                case AnswerType.choice:
                    answers = [row[key] for key in row.keys() if key != "Question"]

                case AnswerType.tf:
                    answers = [True, False]

            self.questions.append(
                Question(row["Question"], answers, index + 1)
            )

    def process_result(self, response: Dict[str, str]) -> Dict:
        pass

    @property
    def info(self):
        if not self.info_path:
            return ""
        return markdown.markdown(open(self.base_path + self.info_path).read())

    @property
    def base_path(self):
        return os.path.dirname(os.path.realpath(__file__)) + "/" + self.name + "/"
