class Solution:
    def findItinerary(self, tickets):
        if not tickets:
            return []
        from_to = {}
        for i in tickets:
            if i[0] in from_to.keys():
                from_to[i[0]].append(i[1])
            else:
                from_to[i[0]] = [i[1]]
        for v in from_to.values():
            v.sort()
        output = ['JFK']
        start = 'JFK'
        while True:
            if start not in from_to.keys():
                break
            elif len(from_to[start])==0:
                break
            else:
                output.append(from_to[start][0])
                temp = start
                start = from_to[start][0]
                from_to[temp].pop(0)
                

        return output

if __name__ == '__main__':
    print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))