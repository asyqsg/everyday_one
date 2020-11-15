
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dic1 = {}
        dic2 = {}
        get_1,get_2 =[],[]
        s1 = list(set(word1))
        s2 = list(set(word2))
        for i in set(word1):
            get_1.append(list(word1).count(i))
        for i in set(word2):
            get_2.append(list(word2).count(i))
        get_1.sort()
        get_2.sort()
        s1.sort()
        s2.sort()
        if get_2 == get_1 and s1 == s2:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Solution().closeStrings("abc","bac"))