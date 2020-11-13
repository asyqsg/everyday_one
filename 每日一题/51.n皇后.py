class Solution:
    def solveNQueens(self, n: int):
        col = set()
        diag1 =set()
        diag2 = set()
        queens = ['-1']*n
        row = ['.']*n
        solution = []

        def get_borad():
            borad = []
            for i in range(n):
                row[queens[i]] = 'Q'
                borad.append(''.join(row))
                row[queens[i]] = '.'
            return borad

        def dfs(row:int):
            if row == n:
                borad = get_borad()
                solution.append(borad)
            else:
                for i in range(n):
                    if i in col or row+i in diag1 or row-i in diag2:
                        continue
                    queens[row] = i
                    diag1.add(row+i)
                    diag2.add(row-i)
                    col.add(i)
                    dfs(row+1)
                    diag1.remove(row+i)
                    diag2.remove(row-i)
                    col.remove(i)

        dfs(0)
        return solution




if __name__ == '__main__':
    print(Solution().solveNQueens(4))

