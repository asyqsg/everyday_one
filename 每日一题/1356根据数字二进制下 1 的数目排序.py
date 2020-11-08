from collections import defaultdict as d
class Solution:
    def sortByBits(self, arr):
        if not arr: return []

        d1 = d(list)
        for i in arr:
            d1[bin(i).count('1')].append(i)      #bin()的返回类型是str
        d1 = sorted(d1.items(),key=lambda x:x[0])
        res = []
        for key,val in d1:
            res.extend(sorted(val))
        return res
if __name__ =='__main__':
    print(Solution().sortByBits([0,1,2,3,4,5,6,7,8]))

