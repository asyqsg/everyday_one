class Solution:
    def partitionLabels(self, S: str):
        if not S: return []

        s = list(S)
        size = len(s)
        res = []
        start = end = i = 0
        while end != size:
            start = end
            i = start
            while i < size:
                temp = s[start:end+1]
                if s[i] in temp:
                    end = i
                i+=1
            end+=1
            temp = ''.join(s[start:end])
            res.append(len(temp))
        return res


if __name__ == '__main__':
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))