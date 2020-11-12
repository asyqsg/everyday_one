class Solution:
    def sortArrayByParityII(self, A):
        size = len(A)
        re_A = []
        if size < 1:
            return []
        stack_ou = []
        stack_ji = []
        for i in A:
            if i%2 == 0:
                stack_ou.append(i)
            else:
                stack_ji.append(i)
        for i in range(size):
            if i%2 == 0:
                temp = stack_ou.pop()
                re_A.append(temp)
            else:
                temp = stack_ji.pop()
                re_A.append(temp)
        return re_A

if __name__ == '__main__':
    print(Solution().sortArrayByParityII([4,2,5,7]))