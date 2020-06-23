# encoding: utf-8
"""
todo: 题目要求：请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。。
https://leetcode-cn.com/problems/daily-temperatures/
"""
from timeit import Timer

#

class Solution(object):
    def dailyTemperatures(slef, T):
        stack = []
        r = [0] * len(T)
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                c = stack.pop()
                r[c] = i - c
            stack.append(i)
        return r


class Solution2(object):
    def dailyTemperatures(self, T):
        res = [0] * len(T)
        for idx1, num1 in enumerate(T):
            for idx2, num2 in enumerate(T[(idx1+1):]):
                # print(num2)
                if num2 > num1:
                    res[idx1] = idx2 + 1
                    break

        return res


if __name__ == "__main__":
    # output result
    output1 = Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(output1)
    output2 = Solution2().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(output2)
    print("\n"*2)
    # performance test
    t1 = Timer("Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])", "from __main__ import Solution")
    print("concat ", t1.timeit(number=1000), "seconds")
    t2 = Timer("Solution2().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])", "from __main__ import Solution2")
    print("concat ", t2.timeit(number=1000), "seconds")

