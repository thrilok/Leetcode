class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        d1 = self.distance(p1, p2)
        d2 = self.distance(p1, p3)
        d3 = self.distance(p1, p4)
        d4 = self.distance(p2, p3)
        d5 = self.distance(p2, p4)
        d6 = self.distance(p3, p4)
        all_length = sorted([d1, d2, d3, d4, d5, d6])
        fourside = False
        diagonal = False
        if all_length[0] == 0:
            return False
        if all_length[0] == all_length[1] == all_length[2] == all_length[3]:
            fourside = True
        diagonal_len = math.sqrt(2) * all_length[0]
        print(all_length, diagonal_len)
        if round(all_length[4], 2) == round(all_length[5], 2) == round(diagonal_len, 2):
            diagonal = True
        if fourside and diagonal:
            return True
        return False
    def distance(self, p1:List[int], p2:List[int]) -> float:
        distance = (math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))
        return distance
       
# Your runtime beats 98.22 % of python3 submissions.
