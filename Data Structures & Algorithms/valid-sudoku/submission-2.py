class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            uniqueNums1 = []
            for rowItem in row:
                if not (rowItem <='9' and rowItem >='1' or rowItem == ".") or (rowItem in uniqueNums1):
                    return False
                else:
                    if rowItem != ".":
                        uniqueNums1.append(rowItem)
        
        for i in range(9):
            uniqueNums2 = []
            for j in range(9):
                if not (board[j][i] <= '9' and board[j][i] >= '1' or board[j][i] == '.') or (board[j][i] in uniqueNums2):
                    return False
                else:
                    if board[j][i] != ".":
                        uniqueNums2.append(board[j][i])
        
        for i in range(3):
            for j in range(3):
                uniqueNums3 = []
                for row in range(0,3):
                    for col in range(0,3):
                        curr = board[3*i+row][3*j+col]
                        if not (curr <= '9' and curr >= '1' or curr == '.') or curr in uniqueNums3:
                            return False
                        else:
                            if curr != ".":
                                uniqueNums3.append(curr)
        
        return True

        
