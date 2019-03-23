class Solution:
    def spiralOrder(self, matrix):
        j,x = 0,1
        l = []
        m = len(matrix)
        n = len(matrix[0])
        while x<=n*m:
            for i in range(j,n-j):
                l.append(matrix[j][i])
                x += 1
            for i in range(j+1,m-j):
                l.append(matrix[i][n-j-1])
                x += 1
            if x <= n * m:
                for i in range(n-j-2,j-1,-1):
                    l.append(matrix[m-j-1][i])
                    x += 1
                for i in range(m-j-2,j,-1):
                    l.append(matrix[i][j])
                    x += 1
            j += 1
        return l

a = Solution()
print(a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))