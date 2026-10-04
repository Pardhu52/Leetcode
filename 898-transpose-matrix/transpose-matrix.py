class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        res=[]
        rows=len(matrix)
        cols=len(matrix[0])

        for j in range(cols):
            mat=[]
            for i in range(rows):
                mat.append(matrix[i][j])
            res.append(mat)
        return res
        