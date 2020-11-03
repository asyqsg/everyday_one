'''
416. 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
'''
class Solution:
    def canPartition(self, nums:list) -> bool:
        size = len(nums)
        if size < 2:
            return False
        sum_nums = sum(nums)
        if sum_nums%2 != 0:
            return False
        nums.sort()
        for i in range(size):
            temp1 = nums[:i]
            temp2 = nums[i:]
            if sum(temp1) == sum(temp2):
                return True
        return False