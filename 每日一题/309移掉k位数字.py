class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        size = len(num)
        remain = size - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k-=1
            stack.append(digit)
        stack = stack[:remain]
        stack = ''.join(stack)
        return str(int(stack))

if __name__ == '__main__':
    print(Solution().removeKdigits("1432219",3))

