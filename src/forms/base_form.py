from typing import Dict
import pandas as pd


class BaseForm:
    name = "base"
    display_name = "Base Test Form"
    questions = []
    path = None

    def __init__(self):
        if self.path:
            self.load()

    def load(self) -> None:
        self.questions = []
        df = pd.read_csv(self.path)
        for index, row in df.iterrows():
            self.questions.append({
                "text": row["Question"],
                "variants": [row[key] for key in row.keys() if key != "Question"],
                "number": index + 1,
            })

    def to_html(self) -> str:
        return self.display_name

    def process_result(self, response: Dict[str, str]) -> str:
        pass

    def label_to_html(self):
        return f"<div class='form-label'><a href='test/{self.name}'><p>{self.display_name}</p></a></div>"
