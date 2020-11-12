class Solution:
    def permute(self, nums):
        res,path = [],[]
        def dfs(nums,path):
            if not nums:
                path = list(path)
                res.append(path)
                return

            for i in range(len(nums)):
                path.append(nums[i])
                dfs(nums[:i]+nums[i+1:],path)
                path.pop()
        dfs(nums,path)
        return res

if __name__ == '__main__':
    print(Solution().permute([1,2,3]))