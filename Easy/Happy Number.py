class Solution:
    def isHappy(self, n: int) -> bool:
        seen_digits = set()
        while n!= 1:
            current = n
            sum_of_digits = 0
            while current !=0:
                rem = current%10
                sum_of_digits += (rem*rem)
                current = current//10
	        # Checking if this going to loop or not
            if sum_of_digits in seen_digits:
                return False
            seen_digits.add(sum_of_digits)
            n = sum_of_digits
        return True

#
