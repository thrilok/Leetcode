class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        initial_color = image[sr][sc]
        columns = len(image)
        rows = len(image[0])
        # To avoid recursion
        if newColor == initial_color:
            return image
        
        def changeColor(x, y):
            if image[x][y] == initial_color:
                image[x][y] = newColor
                if x+1<columns:
                    changeColor(x+1, y)
                if x-1>=0:
                    changeColor(x-1, y)
                if y+1<rows:
                    changeColor(x, y+1)
                if y-1>=0:
                    changeColor(x, y-1)
        changeColor(sr, sc)
        return image
    
# Runtime: 80 ms, faster than 61.63% of Python3 online submissions for Flood Fill.
# Memory Usage: 14.1 MB, less than 5.56% of Python3 online submissions for Flood Fill.
