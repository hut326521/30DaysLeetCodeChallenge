"""We can use DFS and cache to find the result recursively."""
from functools import lru_cache
from collections import Counter

class Solution:
    @lru_cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        if len(s1) == 1:
            return s1 == s2
        s1_left, s1_right = Counter(), Counter(s1)
        s2_xy_left, s2_xy_right = Counter(), Counter(s2)
        s2_yx_left, s2_yx_right = Counter(s2), Counter()
        for boundary in range(len(s1) - 1):
            s1_char = s1[boundary]
            s1_left.update(s1_char)
            s1_right.subtract(s1_char)
            s2_xy_char = s2[boundary]
            s2_xy_left.update(s2_xy_char)
            s2_xy_right.subtract(s2_xy_char)
            s2_yx_char = s2[len(s2) - boundary - 1]
            s2_yx_left.subtract(s2_yx_char)
            s2_yx_right.update(s2_yx_char)
            if s1_left == s2_xy_left and s1_right == s2_xy_right:
                if self.isScramble(
                    s1[:boundary + 1], s2[:boundary + 1]
                ) and self.isScramble(
                    s1[boundary + 1:], s2[boundary + 1:]
                ):
                    return True
            if s1_left == s2_yx_right and s1_right == s2_yx_left:
                if self.isScramble(
                    s1[:boundary + 1], s2[len(s2) - boundary - 1:]
                ) and self.isScramble(
                    s1[boundary + 1:], s2[:len(s2)- boundary - 1]
                ):
                    return True
        return False
