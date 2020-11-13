#效果不太好
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        size = len(s)

        def check(i,j):
            if s[j] in s[i:j]:
                return True #有重复
            else:
                return False

        i = 0
        max_len = 0
        for j in range(size):
            while i <= j or(i <= j and j == size-1):
                if check(i,j):
                    i+=1
                    max_len = max(max_len,j-i+1)
                else:
                    max_len = max(max_len,j-i+1)
                    break

        return max_len

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbb'))