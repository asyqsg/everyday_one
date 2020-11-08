class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack = []
        s = list(s)
        count = 0
        pre_count = 0
        for i in s:
            if i == '(':
                if not stack:
                    pre_count += count
                    count = 0
                stack.append(i)

            elif i == ')':
                if stack:
                    stack.pop()
                    count += 2
                else:
                    pre_count += count
                    count = 0
        return max(pre_count,count)

if __name__ == '__main__':
    print(Solution().longestValidParentheses('()()'))
