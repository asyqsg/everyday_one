class Solution:
    def reversePairs(self, nums) -> int:
        if len(nums) <= 1: return 0

        mid = len(nums)//2
        L = nums[:mid]
        R = nums[mid:]

        ans = self.reversePairs(L) + self.reversePairs(R)

        i,j,k = 0,0,0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i+=1
            else:
                ans += len(L)-i
                nums[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            nums[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            nums[k] = R[j]
            j+=1
            k+=1
        return ans
if __name__ == '__main__':
    print(Solution().reversePairs([7,5,6,4]))