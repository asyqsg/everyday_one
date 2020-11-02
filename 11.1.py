class Solution:
    def wordBreak(self, s: str, wordDict):
        res = []
        wordDict = set(wordDict)

        def dfs(wordDict,temp,pos):
            if pos == len(s):
                res.append(' '.join(temp))
                return
            for i in range(pos,len(s)+1):
                if s[pos:i] in wordDict:
                    temp.append(s[pos:i])
                    dfs(wordDict,temp,i)
                    temp.pop()

        dfs(wordDict,[],0)
        return res


if __name__ == '__main__':
    print(Solution().wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))
