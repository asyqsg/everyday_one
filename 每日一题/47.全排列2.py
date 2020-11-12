class Solution:
    def permuteUnique(self, nums):
        res,path = [],[]
        nums.sort()
        def dfs(nums,path):
            if not nums:
                path = list(path)
                res.append(path)
                return

            for i in range(len(nums)):
                if i == 0:
                    path.append(nums[i])
                elif nums[i] != nums[i-1]:
                    path.append(nums[i])
                else:
                    continue
                dfs(nums[:i]+nums[i+1:],path)
                path.pop()

        dfs(nums,path)
        return res

if __name__ == '__main__':
    print(Solution().permuteUnique([1,1,3]))