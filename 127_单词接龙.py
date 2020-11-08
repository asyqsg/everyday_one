class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        def dfs(cur_list,wordlist):


            def get_wordList(cur:str,wordlist:list):
                cur_list = list(cur)
                new_cur,new_wordlist = [],[]
                for i in wordList:
                    i_list = list(i)
                    temp = cur_list+i_list
                    if len(set(temp)) == 2:
                        new_cur.append(i)
                    else:
                        new_wordlist.append(i)

            for i in cur_list:

