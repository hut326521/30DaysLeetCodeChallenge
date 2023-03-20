from abc import ABC
from typing import Iterable
from unittest import TestCase


class LeetcodeProblemTestCase(TestCase, ABC):
    cases: dict[str, Iterable]
    solution_cls: type[object]
    solution_method_name: str

    def test_solution(self):
        for name, (*args, expected) in self.cases.items():
            with self.subTest(msg=name):
                method = getattr(self.solution_cls(), self.solution_method_name)
                self.assertEquals(method(*args), expected)
