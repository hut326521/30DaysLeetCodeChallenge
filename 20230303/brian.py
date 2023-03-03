"""
The easiest solution is to use str.find() method. Alternatively, we can cut
`haystack` into parts and compare to `needle` one by one.
To be honest, I don't think it's worth our effort to memorize some advanced
algorithms like Knuth–Morris–Pratt pattern matching just to solve this type
of questions.
"""
import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for start in range(len(haystack) - len(needle) + 1):
            if haystack[start:start + len(needle)] == needle:
                return start
        return -1

    def easiest(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class TestSolution(unittest.TestCase):
    def test_strStr_failed_case(self):
        haystack = "a"
        needle = "a"
        result = Solution().strStr(haystack, needle)
        self.assertEqual(result, 0)
