class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(board):
            for i in board:
                s = set()
                for j in i:
                    if j != ".":
                        if j in s:
                            return False
                        s.add(j)
            return True

        def checkCol(board):
            for j in range(len(board[0])):
                s = set()
                for i in range(len(board)):
                    if board[i][j] != ".":
                        if board[i][j] in s:
                            return False
                        s.add(board[i][j])
            return True

        def checkBox(board):
            for r in range(0,9,3):
                for c in range(0,9,3):
                    s = set()
                    for i in range(0,3):
                        for j in range(0,3):
                            if board[i+r][j+c] != ".":
                                if board[i+r][j+c] in s:
                                    return False
                                s.add(board[i+r][j+c])
            return True

        return checkRow(board) and checkCol(board) and checkBox(board)