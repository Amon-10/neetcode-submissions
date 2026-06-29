class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seenInRow = set()

            for element in range(9):
                if board[row][element] == ".":
                    continue
                
                if board[row][element] in seenInRow:
                    return False
                
                seenInRow.add(board[row][element])
        
        for col in range(9):
            seenInColumn = set()

            for element in range(9):
                if board[element][col] == ".":
                    continue
                
                if board[element][col] in seenInColumn:
                    return False
                
                seenInColumn.add(board[element][col])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True