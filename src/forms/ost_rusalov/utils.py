import re
from typing import Dict, Tuple, List


def points_sum(points: Dict[bool, List[int]], response: Dict[int, bool]):
    plus = [1 for el in points[True] if response[el]]
    minus = [1 for el in points[False] if not response[el]]
    return len(plus) + len(minus)


def calculate_parameters(response: Dict[int, bool]):
    return {key: points_sum(value, response) for key, value in parameters.items()}


parameters = {
    "Ергічність (Ер)":
        {
            True: [4, 6, 15, 22, 42, 50, 58, 64, 98],
            False: [27, 83, 103],
        },

    "Соціальна ергічність (СЕр)":
        {
            True: [11, 30, 57, 62, 67, 78, 86],
            False: [3, 34, 74, 90, 105],
        },

    "Пластичність (П)":
        {
            True: [20, 25, 35, 38, 47, 66, 71, 76, 101],
            False: [54, 59],
        },

    "Соціальна пластичність (СП)":
        {
            True: [2, 9, 18, 26, 45, 68, 85, 99],
            False: [31, 81, 87, 93],
        },

    "Темп (Т)":
        {
            True: [1, 13, 19, 33, 46, 49, 55, 77],
            False: [29, 43, 70, 94],
        },

    "Соціальний темп (СТ)":
        {
            True: [24, 37, 39, 51, 72, 92],
            False: [5, 10, 16, 56, 96, 102],
        },

    "Емоційність (Ем)":
        {
            True: [14, 17, 28, 40, 60, 61, 79, 88, 91, 95, 97],
            False: [],
        },

    "Соціальна емоційність (СЕм)":
        {
            True: [6, 7, 21, 36, 41, 48, 53, 63, 75, 80, 84, 100],
            False: [],
        },

    "Контрольні запитання на соціальну бажаність (К)":
        {
            True: [32, 52, 89],
            False: [12, 23, 44, 65, 73, 82],
        },
}
