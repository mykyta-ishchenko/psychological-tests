from typing import Dict
import pandas as pd
from .models import Question, AnswerType


class BaseForm:
    name = "base"
    display_name = "Base Test Form"
    questions = []
    type = AnswerType.choice
    path = None
    processing_info = ""

    def __init__(self):
        if self.path:
            self.load()

    def load(self) -> None:
        self.questions = []
        df = pd.read_csv(self.path)
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

    def to_html(self) -> str:
        return self.display_name

    def process_result(self, response: Dict[str, str]) -> str:
        pass
