# encoding: utf-8
"""
https://leetcode-cn.com/problems/group-anagrams/
todo: 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
eg:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
"""
from timeit import Timer

class Solution(object):
    def groupAnagrams(self, strs: list) -> list:
        dic = {}
        res =[]
        for i in strs:
            dic.setdefault(str(sorted(i)),[]).append(i)
        for value in dic.values():
            res.append(value)
        return res

class Solutions(object):
    def group_str(self, strs):
         res = dict()
         map(lambda x: res.get(str(sorted(x)), []).append(x), strs)
         return list(res.values())


if __name__ == "__main__":
    input = ["eat", "tea", "t an", "ate", "nat", "bat"]
    # res = Solution().groupAnagrams(input)
    t1 = Timer("Solution().groupAnagrams("+str(input)+")", "from __main__ import Solution")
    print("res", t1.timeit(number=10000), "seconds")

    t2 = Timer("Solutions().group_str("+str(input)+")", "from __main__ import Solutions")
    print("res", t2.timeit(number=10000), "seconds")

