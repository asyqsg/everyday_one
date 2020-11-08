class Solution:
    def minDeletions(self, s: str) -> int:
        hash = {}
        number = []
        s = list(s)
        count = 0
        for i in s:
            hash[i] = hash.get(i,0)+1
        for key,val in hash.items():
            number.append(val)
        number.sort()
        for i in range(1,len(number)):
            if number[i] == number[i-1]:
                while number[i] > 0:
                    number[i] -= 1
                    count += 1
                    if number[i] not in number[:i]:
                        number.sort()
                        break
                    else:
                        number.sort()




        return count

if __name__ == '__main__':
    print(Solution().minDeletions("adec"))