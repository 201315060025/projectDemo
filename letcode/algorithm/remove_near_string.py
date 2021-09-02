# encoding: utf-8
"""
删除相邻重复项字符串： https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

 

示例：

输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

"""
from timeit import Timer


class Solution:

    def removeDuplicates(self, S: str) -> str:
        "使用迭代"
        s_list = list(S)
        repeat_idx, repeat_flag, last_num = [], False, None
        for idx, num in enumerate(s_list):
            if idx == 0:
                last_num = num
                continue
            if last_num == num:
                repeat_flag = True
                repeat_idx.append([idx-1, idx])
                break
            last_num = num
        if repeat_flag:
            new_s_list = list([num for idx, num in enumerate(s_list) if idx not in repeat_idx[0]])
            s_list = self.removeDuplicates("".join(new_s_list))
        return "".join(s_list)

    def remove_duplicate(self, string_obj: str)->str:
        """"""
        new_s = [""]
        for s in string_obj:
            if new_s[-1] == s:
                new_s.pop()
            else:
                new_s.append(s)
        return "".join(new_s)


if __name__ == "__main__":
    tmp_s = "abbaca"
    res = Solution().removeDuplicates(tmp_s)
    print(res)

    res = Solution().remove_duplicate(tmp_s)
    print(res)

    t1 = Timer('Solution().removeDuplicates("abbaca")', "from __main__ import Solution")
    print("result", t1.timeit(number=1000), "seconds")
    t2 = Timer('Solution().remove_duplicate("abbaca")', "from __main__ import Solution")
    print("result", t2.timeit(number=1000), "seconds")