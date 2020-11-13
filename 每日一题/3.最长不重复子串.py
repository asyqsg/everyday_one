class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        def check(my_list:list,j):
            nonlocal max_len
            if s[j] in my_list:
                index = my_list.index(s[j])
                my_list = my_list[index+1:]
            my_list.append(s[j])
            max_len = max(max_len,len(my_list))
            return my_list
        my_list = []
        for j in range(len(s)):
            my_list = check(my_list,j)
        return max_len

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('aab'))
