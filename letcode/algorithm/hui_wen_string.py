# encoding: utf-8
"""
回文字符串
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:
Input: "cbbd"
Output: "bb"
"""
from timeit import Timer

class Solution(object):
    def hui_wen(self, str_obj: str):
        max_hui_wen = ""
        for idx1, str1 in enumerate(str_obj):
            hui_wen_str = str1
            for idx2, str2 in enumerate(str_obj[idx1+1:]):
                hui_wen_str += str2
                if hui_wen_str == hui_wen_str[::-1] and len(max_hui_wen) < len(hui_wen_str):
                    max_hui_wen = hui_wen_str

        return max_hui_wen


class Solution2(object):
    def hui_wen(self, s: str) -> str:
        r = ''
        for i, j in [(i, j) for i in range(len(s)) for j in (0, 1)]:
            while i > -1 and i + j < len(s) and s[i] == s[i + j]: i, j = i - 1, j + 2
            r = max(r, s[i + 1:i + j], key=len)
        return '' if not s else r

if __name__ == "__main__":
    st = "cbbd"
    t1 = Timer("Solution().hui_wen('"+st+"')", "from __main__ import Solution")
    print("res", t1.timeit(number=1000), "seconds")


    t2 = Timer("Solution2().hui_wen('"+st+"')", "from __main__ import Solution2")
    print("res", t2.timeit(number=1000), "seconds")



