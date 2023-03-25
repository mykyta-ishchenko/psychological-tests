from dataclasses import dataclass
from enum import Enum


class AnswerType(Enum):
    tf = "true_or_false"
    choice = "choice"


@dataclass
class Question:
    text: str
    variants: list
    number: int = None
