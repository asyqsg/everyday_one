#前缀和和后缀和
class Solution:
    def minOperations(self, nums, x: int) -> int:
        if sum(nums) < x: return -1
        left = 0
        L_sum = {}
        for i in range(len(nums)):
            left += nums[i]
            if left > x: break
            L_sum[left] = i+1

        right = 0
        R_sum = {}
        for i in range(len(nums)-1,-1,-1):
            right += nums[i]
            if right > x: break
            R_sum[right] = len(nums)-i

        cur = min(L_sum.get(x,float('inf')),R_sum.get(x,float('inf')))

        for i in L_sum:
            if x - i in R_sum:
                temp = L_sum[i] + R_sum[x-i]
                cur = min(temp,cur)
        return cur

if __name__ == '__main__':
    print(Solution().minOperations([1,1,4,2,3],5))