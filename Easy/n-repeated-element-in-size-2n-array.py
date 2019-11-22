class Solution:
	def repeatedNTimes(self, A: List[int]) -> int:
		hash_table ={
		
		}
		length = len(A)
		for x in range(0, length):
			try:
				hash_table.pop(A[x])
				return A[x]
			except:
				hash_table[A[x]] =1
			
	
	# def solution2(self, A):
	# 	length = len(A)
	# 	for x in range(0, 4):
	# 		for y in range(0, length):
	# 			if A[y] == A[y+x]:
	# 				return A[y]
