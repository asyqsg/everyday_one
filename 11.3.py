'''
山脉
easy
'''
class Solution:
    def validMountainArray(self, A:list) -> bool:
        if not A: return False

        size = len(A)
        if size < 3: return False
        have_up,have_down = False,False
        up = 0
        peak = 0
        while up < size-1:
            if A[up] < A[up+1]:
                have_up = True
                up+=1
            else:
                peak = up
                break
        if not have_up: return False

        down = peak
        while down < size-1:
            if A[down] > A[down+1]:
                have_down = True
                down += 1
            else:
                return False
        if have_down and have_up:
            return True