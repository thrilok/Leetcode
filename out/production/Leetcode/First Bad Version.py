# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        answer = False
        returnValue = n
        while not answer:
            mid = (left+right)//2
            if isBadVersion(mid):
                if returnValue > mid:
                    returnValue = mid
                elif returnValue == mid:
                    return returnValue
                right = mid
                mid = (left+right)//2
            else:
                left = mid+1
                mid = (left+right)//2
                
# Runtime: 28 ms, faster than 68.65% of Python3 online submissions for First Bad Version.
# Memory Usage: 13.7 MB, less than 6.90% of Python3 online submissions for First Bad Version.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        answer = False
        returnValue = n
        while left< right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left

# Runtime: 32 ms, faster than 31.73% of Python3 online submissions for First Bad Version.
# Memory Usage: 13.9 MB, less than 6.90% of Python3 online submissions for First Bad Version


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        answer = False
        returnValue = n
        while left< right:
            mid = left+(right-left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left

# Runtime: 24 ms, faster than 89.42% of Python3 online submissions for First Bad Version.
# Memory Usage: 13.8 MB, less than 6.90% of Python3 online submissions for First Bad Version.
