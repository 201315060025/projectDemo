# encoding: utf-8
"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组
eg:
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
import timeit

class Solutions(object):
    def three_sum(self, nums):
        for id1, num1 in enumerate(nums):
            for id2, num2 in enumerate(nums):
                for id3, num3 in enumerate(nums):
                    if id1 == id2 == id3:
                        continue
                    if num1 + num2 + num3 == 0 and id3>id2>id1:
                        print(num1, num2, num3)


class Solution3(object):
    def three_sum(self, nums, target):
        """
        1: 判断长度 是否满足3个，否则直接返回
        2：排序
        3：开始循环，索引，
        4：
        :param nums:
        :return:
        """
        if not nums: return 0
        if len(nums) < 3: return sum(nums)
        nums.sort()
        res = float("inf")
        for i in range(len(nums)):
            if i> 0: continue
            left = i +1
            right = len(nums) - 1
            while left < right:
                cur_num = nums[i] + nums[left] + nums[right]
                if cur_num == target:return cur_num
                if abs(cur_num - target) < abs(res-target):
                    res = cur_num
                if cur_num - target> 0:
                    right -= 1
                else:
                    left += 1


        return res


if __name__ == "__main__":
    num = [-1,3,1,-4,4]
    # [-4,-1,1,3,4]
    t1 = timeit.Timer("Solution3().three_sum([-1,3,1,-4,4], 1)", "from __main__ import Solution3")
    print("res", t1.timeit(number=1000), "seconds")

    t2 = timeit.Timer("Solutions().three_sum([-1,3,1,-4,4], 1)", "from __main__ import Solutions")
    print("res", t2.timeit(number=1000), "seconds")
