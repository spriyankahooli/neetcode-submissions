class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        bottom, right  = len(matrix)-1,len(matrix[0])-1
        top,left =0,0 
        res= []
        while top <= bottom and left <= right:
            for c in range(left, right+1):
                res.append(matrix[top][c])
            top+=1

            for r in range(top,bottom+1):
                res.append(matrix[r][right])
            right-=1

            if top <= bottom:
                for c in range(right,left-1,-1):
                    res.append(matrix[bottom][c])
                bottom-=1
            if left <= right:
                for r in range(bottom,top-1,-1):
                    res.append(matrix[r][left])
                left+=1
        return res
       