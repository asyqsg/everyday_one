from collections import defaultdict as d
class Solution:
    def relativeSortArray(self, arr1:list, arr2):
        size = len(arr1)
        d = {}
        for i in arr1:
            d[i] = d.get(i,0)+1
        output = []
        for i in arr2:
            temp = [i]*d[i]
            output.extend(temp)
        d2 = []
        for i in arr1:
            if i not in arr2:
                d2.append(i)
        output.extend(d2)
        return output
if __name__ == '__main__':
    print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))

