class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        col=set()
        diag=set()
        anti_diag=set()
        col_q_row=[-1]*n

        def backtrack(row):
            if row==n:
                board=[]
                for i in range(n):
                    row_str="." * col_q_row[i] + "Q" +"." * (n-col_q_row[i]-1)
                    board.append(row_str)
                res.append(board)
                return
            for c in range(n):
                if c in col or (row-c) in diag or (row+c) in anti_diag:
                    continue

                col.add(c)
                diag.add(row-c)
                anti_diag.add(row+c)
                col_q_row[row]=c

                backtrack(row+1)

                col.remove(c)
                diag.remove(row-c)
                anti_diag.remove(row+c)

        backtrack(0)
        return res







