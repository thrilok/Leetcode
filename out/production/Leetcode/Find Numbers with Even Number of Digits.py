class Solution:
	def findNumbers(self, nums: List[int]) -> int:
		count = 0
		length = len(nums)
		for x in range(0, length):
			n = nums[x]
			digit_count = 0
			while n>0:
				digit_count +=1
				n = int(n/10)
			if digit_count%2 == 0:
				count +=1
		return count
	
# Runtime: 64 ms, faster than 9.41% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.


class Solution:
	def findNumbers(self, nums: List[int]) -> int:
		count = 0
		length = len(nums)
		for x in range(0, length):
			n = nums[x]
			digit_count = 0
			while n>0:
				digit_count +=1
				n = int(n/10)
			if digit_count%2 == 0:
				count +=1
		return count

# Runtime: 76 ms, faster than 5.11% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.
