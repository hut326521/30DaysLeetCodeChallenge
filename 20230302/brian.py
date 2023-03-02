"""
We can use a pointer "write" to help us track which index in the input array to
we need to update while we iterate through the original series of characters.
"""
from typing import List
from unittest import TestCase


class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        count = 1
        for read in range(len(chars)):
            # not the last one and in the middle of a series
            if read < len(chars) - 1 and chars[read] == chars[read + 1]:
                count += 1
                continue
            # reach last one or end of a series
            chars[write] = chars[read]  # letter
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            # reset count
            count = 1
        return write


class TestSolution(TestCase):
    def test_compress_with_sample_data(self):
        cases = [
            (["a", "a", "b", "b", "c", "c", "c"], ["a", "2", "b", "2", "c", "3"], 6),
            (["a"], ["a"], 1),
            (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], ["a", "b", "1", "2"], 4),
        ]
        for chars, compressed, length in cases:
            with self.subTest(chars=chars, compressed=compressed, length=length):
                result = Solution().compress(chars)
                self.assertEqual(result, length)
                self.assertEqual(chars[:length], compressed)

    def test_compress_with_single_digit_ending(self):
        chars = ["a", "a", "b", "b", "c", "c", "c", "d"]
        compressed = ["a", "2", "b", "2", "c", "3", "d"]
        length = 7

        result = Solution().compress(chars)
        self.assertEqual(result, length)
        self.assertEqual(chars[:result], compressed)
