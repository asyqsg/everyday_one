class Solution:
    def insert(self, intervals: list, newInterval: list):
        if not intervals: return [newInterval]
        if not newInterval: return intervals

        start,end = newInterval[0],newInterval[1]
        output = []
        temp = []
        for i in intervals:
            unstart = i[0]
            unend = i[1]
            if unstart > end or unend < start:
                output.append(i)
            else:
                temp.append(unstart)
                temp.append(unend)
        if temp:
            temp.append(start)
            temp.append(end)
            temp.sort()
            temp = [temp[0],temp[-1]]
            output.append(temp)
        else:
            output.append(newInterval)
        output = sorted(output,key=lambda x:x[0])

        return output

if __name__ == '__main__':
    print(Solution().insert([[1,3],[6,9]],[2,5]))

