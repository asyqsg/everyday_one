'''
给定一个包含n 个整数的数组nums和一个目标值target，判断nums中是否存在四个元素 a，b，c和 d，使得a + b + c + d的值与
target相等？找出所有满足条件且不重复的四元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def fourSum(self, nums, target: int):
        size = len(nums)
        if size < 4: return []
        res,path = [],[]
        nums.sort()

        def dfs(nums:list):
            if len(path) == 4:
                if sum(path) == target and path not in res:
                    res.append(list(path))
                return

            for i in nums:
                path.append(i)
                

