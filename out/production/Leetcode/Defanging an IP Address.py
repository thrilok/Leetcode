class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_string = ''
        length = len(address)
        for x in range(0, length):
            if address[x]=='.':
                new_string+='[.]'
            else:
                new_string+= address[x]
        return new_string

# Runtime: 24 ms, faster than 84.05% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.


