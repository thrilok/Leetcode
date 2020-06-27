class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = minutes*6
        if hour==12:
            hour = 0
        hour_angle = (minutes*0.5)+(hour*30)
        result = abs(min_angle-hour_angle)
        return min(result, 360-result)
		
# Runtime: 32 ms, faster than 36.74% of Python3 online submissions for Angle Between Hands of a Clock.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Angle Between Hands of a Clock.
