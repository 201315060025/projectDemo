# encoding: utf-8
"""
https://leetcode-cn.com/problems/two-sum/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china
todo: 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

eg：
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
from timeit import Timer


class Solution(object):
    def two_sum(self, nums: list, target) -> list:
        for idx1, num in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if idx1 == idx2:
                    continue
                if (num + num2) == target:
                    return [idx1, idx2]

class Solution2(object):
    def two_sum(self, nums: list, target:int)->list:
        for idx, num in enumerate(nums):
            num_other  = target - num
            if num_other in (nums):return [idx, nums.index(num_other)]
            else:
                continue


if __name__ == "__main__":
    target = 9
    input = [2, 7, 11, 15]
    t1 = Timer("Solution().two_sum("+str(input)+", "+str(target)+")", "from __main__ import Solution")
    print("res", t1.timeit(number=1000), "seconds")
    print("\n"*2)
    t2 = Timer("Solution2().two_sum("+str(input)+", "+str(target)+")", "from __main__ import Solution2")
    print("res", t2.timeit(number=1000), "seconds")