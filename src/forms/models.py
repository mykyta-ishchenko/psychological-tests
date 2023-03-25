import os
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, List

import markdown


class AnswerType(Enum):
    tf = "true_or_false"
    tfm = "false_or_true_or_maybe"
    choice = "choice"


@dataclass
class Question:
    text: str
    variants: list
    number: int = None


class ProcessingTF:
    def __init__(self, tf: Dict[str, Dict[bool, List[int]]], response: Dict[str, str]):
        self.tf = tf
        self.response = response.copy()

    @staticmethod
    def calculate_param(points: Dict[bool, List[int]], response: Dict[int, bool]):
        res = 0
        for key, lst in points.items():
            for el in lst:
                if isinstance(el, Iterable) and response.get(el[0]) == key:
                    res += el[1]
                elif response.get(el) == key:
                    res += 1
        return res

    def process(self):
        response = {int(key): True if val == "true" else False for key, val in self.response.items()}
        return {key: (self.calculate_param(value, response),) for key, value in self.tf.items()}
