from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class NameCountDictHtml:
    dictionary: Dict[str, Any]
    clas: str = ''

    def to_html(self):
        body = f"<div class='{self.clas}'>"
        for name, count in self.dictionary.items():
            body += f"""
            <div class="sub">
                <div class="name">
                    <p>{name}:</p>
                </div>
                <div class="count">
                    <p>{count}</p>
                </div>
            </div>
            """
        body += "</div>"
        return body


@dataclass
class NameCountHtml:
    name: str
    count: int
    other: Any = ''
    clas: str = ''

    def to_html(self):
        return f"""
        <div class="{self.clas}">
            <div class="name">
                <p>{self.name}:</p>
            </div>
            <div class="count">
                <p>{self.count}</p>
            </div>
            {"<div class='other'>" + self.other + "</div>" if self.other else ""}
        </div>
        """


@dataclass
class NumerateQuestionSingleAnswerHtml:
    questions: list

    def to_html(self):
        body = ""

        for question in self.questions:
            variants = ""

            for index, variant in enumerate(question["variants"]):
                variants += f"""
                <input class="btn-check" type="radio" id="{question["number"]}_{index}" name="{question["number"]}" 
                    value="{index}" {"checked" if index == 0 else ""}>
                <label class="btn text-black btn-outline-warning" for="{question["number"]}_{index}">{variant}</label>
                """

            body += f"""
            <div class="question">
                <div class="question-text">
                    <p>{question["number"]}. {question["text"]}</p>
                </div>
                <div class="variants btn-group" role="group">
                    {variants}
                </div>
            </div>
            """
        # required
        return body


@dataclass
class TextFieldHtml:
    text: str
    clas: str

    def to_html(self):
        return f"""
        <div class="{self.clas}">
            <p>{self.text}</p>
        </div>
        """
