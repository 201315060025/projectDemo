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

class Solution(object):
    def hui_wen(self, str_obj: str):
        for i in range(len(str_obj)):
            for idx, str  in enumerate(str_obj[:i]):
                if str_obj[:i][:idx] == str_obj[:i][:idx][::-1]:
                    print(str_obj[:idx])






        pass