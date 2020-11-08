class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        size = len(nums)
        if size == 0: return 0
        # if size == 1:
        #     if nums[0] >= lower and nums[0] <= upper:
        #         return 1
        count = 0
        for i in range(size):
            for j in range(i+1,size+1):
                temp  = sum(nums[i:j])
                if temp >= lower and temp <= upper:
                    count+=1
        return count

if __name__ == '__main__':
    print(Solution().countRangeSum([0,0],0,0))