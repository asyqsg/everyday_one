import math
from collections import defaultdict as d
class Solution:
    def kClosest(self, points, K: int):
        if not points or not K: return []

        dict = d(list)

        for i in points:
            lenght = math.sqrt(i[0]**2+i[1]**2)
            dict[lenght].append(i)
        dict = sorted(dict.items(),key=lambda x:x[0])
        res = []
        for item in dict:
            res.extend(item[1])
        len_res = len(res)
        return res[:K]

    def kClosest_answer(self, points, K: int):
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:K]

if __name__ == '__main__':
    print(Solution().kClosest([[1,3],[-2,2]],1))