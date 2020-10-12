class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        length = len(emails)
        for x in range(0, length):
            email = emails[x].split("@")
            firstname = email[0]
            firstname = firstname.split("+")[0]
            firstname = firstname.replace(".","" )
            emails[x] = firstname+"@"+email[1]
        return len(set(emails))

# Runtime: 52 ms, faster than 97.32% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 13.8 MB, less than 6.25% of Python3 online submissions for Unique Email Addresses.
