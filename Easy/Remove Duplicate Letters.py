class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = []
        frequency = Counter(s)
        added = set()
        for ch in s:
            frequency[ch] -=1
            if ch in added:
                continue
            while result and result[-1] > ch and frequency[result[-1]]>0:
                added.remove(result.pop())
            if ch not in added:
                result.append(ch)
                added.add(ch)
        return (''.join(result))

# Runtime: 32 ms, faster than 89.59% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Remove Duplicate Letters.
