from collections import Counter as c
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = list(t)
        dict_t = dict(c(t))
        def check(my_list,j):
            nonlocal max_len
            if


        max_len = 0
        my_list = []
        for i in range(len(s)):








if __name__ == '__main__':
    print(Solution().minWindow("ADOBECODEBANC","ABC"))






