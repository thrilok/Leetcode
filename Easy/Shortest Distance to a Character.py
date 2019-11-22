class Solution:
	def shortestToChar(self, S: str, C: str) -> List[int]:
		length_of_string = len(S)
		result = [1] * length_of_string
		i = length_of_string
		j = 0
		current = 0
		x = 0
		for x in range(0, length_of_string):
			if S[x] == C:
				while current <= x:
					result[current] = min([abs(i - current), abs(current - x)])
					current += 1
				i = x
		if i != x:
			temp = 1
			while i < length_of_string - 1:
				result[i + 1] = temp
				temp += 1
				i += 1
		return result

# Runtime: 44 ms, faster than 92.43% of Python3 online submissions for Shortest Distance to a Character.
# Memory Usage: 13.9 MB, less than 7.69% of Python3 online submissions for Shortest Distance to a Character.
