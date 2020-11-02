'''
139. 单词拆分   难度：中等
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
'''

#使用dp来解决
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        size = len(s)
        dp = [False for i in range(size+1)]
        dp[0] = True


        #注意在字符串比较的时候for循环的边界问题
        for i in range(size):
            for j in range(i+1,size+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]