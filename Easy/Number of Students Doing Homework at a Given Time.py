class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        length = len(startTime)
        count = 0
        for x in range(length):
            if startTime[x]<=queryTime:
                if endTime[x]>=queryTime:
                    count+=1
        return count
 
# Runtime: 36 ms, faster than 73.03% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
