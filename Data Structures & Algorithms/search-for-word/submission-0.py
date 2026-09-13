class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col=len(board), len(board[0])

        def backtrack(r,c,i):
            if len(word)==i:
                return True
            if r<0 or r>=row or c<0 or c>=col:
                return False
            if word[i]!=board[r][c]:
                return False
            
            temp=board[r][c]
            board[r][c]="#"

            found=(backtrack(r+1,c,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r,c-1,i+1))

            board[r][c]=temp
            return found

        for i in range(row):
            for c in range(col):
                if backtrack(i,c,0):
                    return True
        return False
