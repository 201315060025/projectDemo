# encoding: utf-8
"""
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
"""
from timeit import Timer

class Solution(object):
    def max_son_str(self, str_obj: str) -> str:
        max_str = ""
        for idx1, st1 in enumerate(str_obj):
            tmp_str = st1
            for idx2, st2 in enumerate(str_obj[idx1+1:]):
                if st2 in tmp_str:
                    max_str = tmp_str if len(tmp_str) > len(max_str) else max_str
                    break
                tmp_str += st2
        return max_str


class Solution2(object):
    def max_son_str(self, s: str) -> int:
        i, r, d = 0, 0, {}
        for j, c in enumerate(s): i, r, d[c] = max(i, d.get(c, -1) + 1), max(r, j - i), j
        return max(r, len(s) - i)


class Solution3(object):
    def max_son_str(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res


if __name__ == "__main__":
    t1 = Timer('Solution().max_son_str("abcabcbb")', "from __main__ import Solution")
    print("res", t1.timeit(number=1000), "seconds")

    t2 = Timer('Solution2().max_son_str("abcabcbb")', "from __main__ import Solution2")
    print("res", t2.timeit(number=1000), "seconds")

    t3 = Timer('Solution3().max_son_str("abcabcbb")', "from __main__ import Solution3")
    print("res", t3.timeit(number=1000), "seconds")

