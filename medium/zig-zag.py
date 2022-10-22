class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = 0
        row_wise = ['']*numRows
        reverse = False
        if numRows == 1:
            return s
        for i, j in enumerate(s):
            row_wise[rows] += j
            if reverse:
                rows -= 1
            else:
                rows += 1
            
            if rows == numRows:
                rows -= 2
                reverse = True
            if rows == -1:
                reverse=False
                rows = 1
        output = ''
        for i in row_wise:
            output += i
        return output
