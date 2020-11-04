class Solution:
    def commonChars(self, A):
        if not A or len(A) == 1: return list(A)
        res = []
        size = len(A)
        for i in range(1,size):
            if i == 1:
                temp = list(A[0])
                temp_i = list(A[i])
                for j in temp_i:
                    if j in temp:
                        res.append(j)
                        temp.remove(j)
                        # temp_i.remove(j)
            else:
                temp_i = list(A[i])
                temp = res
                res = []
                for j in list(A[i]):
                    if j in temp:
                        temp.remove(j)
                        # A[i].remove(j)
                        res.append(j)
        return res

if __name__ == '__main__':
    print(Solution().commonChars(["cool","lock","cook"]))