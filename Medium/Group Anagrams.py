class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words= {
        
        }
        for x in strs:
            sorted_word = ''.join(sorted(x))
            try:
                words[sorted_word].append(x)
            except:
                words[sorted_word] = [x]
        output = []
        for key in words:
            output.append(words[key])
        return output

# Runtime: 104 ms, faster than 70.70% of Python3 online submissions for Group Anagrams.
# Memory Usage: 16.6 MB, less than 43.40% of Python3 online submissions for Group Anagrams

