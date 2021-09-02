# encoding: utf-8
"""
https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
todo:有效的运算符包括 +, -, *, / 。每个运算对象可以是整数,也可以是另一个逆波兰表达式。
说明：
整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说,表达式总会得出有效数值且不存在除数为 0 的情况。
输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: 该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释:
该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
### 解题思路
# 循环 列表 （先进先出）
# 栈 先进后出

pop_list = []
class Solution(object):

    def evalRpn(self, tokens: list) -> int:
        for token in tokens:
            if token in "+-*/":
                num1 = pop_list.pop()
                num2 = pop_list.pop()
                # 此处的 num2 和 num1 不能颠倒
                pop_list.append(str(int(eval((num2+token+num1)))))
                pass
            else:
                pop_list.append(token)
        return int(pop_list[0])

# class Solution:
#     def evalRpn(self, tokens) -> int:
#         PopList = []
#         for i in tokens:
#             if i in "+-*/":
#                 tmp = PopList.pop()
#                 tmp2 = PopList.pop()
#                 PopList.append(str(int(eval(tmp2+i+tmp))))
#             else:
#                 PopList.append(i)
#         return int(PopList[0])



res = Solution().evalRpn(["1","4", "5", "2", "+", "+", "+", "3","-", "6", "8","+", "+"])
print(res)