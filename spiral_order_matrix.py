class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        rows = len(A)
        columns = len(A[0])
        topRow = 0
        bottomRow = rows - 1
        leftMostColumn = 0
        rightMostColumn = columns - 1
        direction = 0
        ## Actual code to populate result
        while topRow <= bottomRow and leftMostColumn <= rightMostColumn:
            if (direction == 0):
                for i in range(leftMostColumn, rightMostColumn + 1):
                    result.append(A[topRow][i])
                topRow += 1
                direction = 1
            elif direction == 1:
                for i in range(topRow, bottomRow + 1):
                    result.append(A[i][rightMostColumn])
                rightMostColumn -= 1
                direction = 2
            elif direction == 2:
                for i in range(rightMostColumn, leftMostColumn - 1, -1):
                    result.append(A[bottomRow][i])
                bottomRow -= 1
                direction = 3
            else:
                for i in range(bottomRow, topRow - 1, - 1):
                    result.append(A[i][leftMostColumn])
                leftMostColumn += 1
                direction = 0
        return result
        
        
arr = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

result = Solution()
print result.spiralOrder(arr)
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
