from collections import Counter as c
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        size = len(s)
        t = list(t)
        array1 = []
        array2 = []
        dict_t = c(t)
        def check(j,i):


        max_lenght = 0
        for i in range(size):
            if s[i] in t:
                array1.append(s[i])
                array2.append(i)

        for i in len(array1):



