'''
太难了！！！！
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = list(s)
        size = len(s)
        if size < 2: return 0
        dp = [0 for i in range(size)]
        for i in range(size):
            if s[i] == '(':
                dp[i] = 0
            else:
                if i == 0:
                    dp[i] = 0
                else:
                    if s[i-1] == ')':
                        index = i-dp[i-1]-1
                        if index >= 0:
                            if s[index] == '(':
                                index2 = index-1
                                if index2>=0:
                                    dp[i] = dp[index2] + dp[i-1] + 2
                                else:
                                    dp[i] = dp[i-1]+2
                        else:
                            dp[i] = 0
                    else:
                        index = i-2
                        dp[i] = dp[index] + 2
        return max(dp)
if __name__ == '__main__':
    print(Solution().longestValidParentheses('())'))
