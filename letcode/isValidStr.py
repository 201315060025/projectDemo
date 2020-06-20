# encoding: utf-8
"""
todo: 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
https://leetcode-cn.com/problems/valid-parentheses/
"""
"""
算法逻辑
判断是否是有效的字符串 return True/False
1: 将规则放到一个字典中（哈希）
2: 然后通过循环找出是否存在
3: 充分利用栈的特点
"""
from timeit import Timer


class Solution(object):
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        # 注意字典的设计
        # dic = {'(': ')', '[': ']', '{': '}'} # wrong dict
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack

class Solution2(object):
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = []
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False
        return len(stack) == 0


if __name__ == '__main__':
    # test
    test1 = "{()[()]}"
    test2 = "((((((("
    print(Solution().isValid(test1))
    print(Solution2().isValid(test2))
    print("\n"*2)
    # test
    t1 = Timer('Solution().isValid("{()[()]}")', "from __main__ import Solution")
    print("result", t1.timeit(number=1000), "seconds")
    t2 = Timer('Solution2().isValid("{()[()]}")', "from __main__ import Solution2")
    print("result", t2.timeit(number=1000), "seconds")