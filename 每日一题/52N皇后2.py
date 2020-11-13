class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        diag1 =set()
        diag2 = set()

        count = 0

        def dfs(row:int):
            nonlocal count
            if row == n:
                count+=1
            else:
                for i in range(n):
                    if i in col or row+i in diag1 or row-i in diag2:
                        continue
                    col.add(i)
                    diag1.add(row+i)
                    diag2.add(row-i)
                    dfs(row+1)
                    col.remove(i)
                    diag1.remove(row+i)
                    diag2.remove(row-i)
        dfs(0)
        return count
if __name__ == '__main__':
    print(Solution().totalNQueens(4))