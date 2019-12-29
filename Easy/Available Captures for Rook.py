class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for x in range(0, 8):
            for y in range(0, 8):
                if board[x][y] == "R":
                    found = [x, y]
                    break
        horizontal = board[found[0]]
        vertical = []
        y = found[1]
        for x in range(0, 8):
            vertical.append(board[x][y])
        temp_x = found[1]+1
        result = 0
        while temp_x <8:
            if horizontal[temp_x] == 'p':
                result +=1
                break
            elif horizontal[temp_x] == '.':
                temp_x +=1
            else:
                break
        temp_x = found[1]-1
        while temp_x >0:
            if horizontal[temp_x] == 'p':
                result +=1
                break
            elif horizontal[temp_x] == '.':
                temp_x -=1
            else:
                break
        temp_y = found[0]+1
        while temp_y <8:
            if vertical[temp_y] == 'p':
                result +=1
                break
            elif vertical[temp_y] == '.':
                temp_y +=1
            else:
                break
        temp_y = found[0]-1
        while temp_y >0:
            if vertical[temp_y] == 'p':
                result +=1
                break
            elif vertical[temp_y] == '.':
                temp_y -=1
            else:
                break
        return result

# Runtime: 20 ms, faster than 99.37% of Python3 online submissions for Available Captures for Rook.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Available Captures for Rook.


