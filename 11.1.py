class Solution:
    def wordBreak(self, s: str, wordDict):
        res = []
        demo = [1] * (len(s)+1)
        wordDict = set(wordDict)

        def dfs(wordDict,temp,pos):
            nums = len(res)
            if pos == len(s):
                res.append(' '.join(temp))
                return
            for i in range(pos,len(s)+1):
                if s[pos:i] in wordDict and demo[i]:
                    temp.append(s[pos:i])
                    dfs(wordDict,temp,i)
                    temp.pop()
            demo[pos] = 1 if len(res) > nums else 0


        dfs(wordDict,[],0)
        return res


if __name__ == '__main__':
    print(Solution().wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))
