class Solution:
    def exist(self, board, word):
        idx = 0
        n = len(board)
        m = len(board[0])
        def check(i, j, idx):
            print(i, j, board)
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != word[idx]:
                return False
            temp = board[i][j]
            board[i][j] = ''
            idx += 1
            print(True)
            if check(i+1, j, idx) or check(i-1, j, idx) or check(i, j+1, idx) or check(i, j-1, idx):
                return True
            board[i][j] = temp
            return False
        for i in range(n):
            for j in range(m):
                print("--------------")
                if check(i, j, 0):
                    return True
        return False
s = Solution()
print(s.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))