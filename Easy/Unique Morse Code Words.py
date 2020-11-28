class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for x in words:
            morse_word = ''
            for char in x:
                morse_word += morse_code[ord(char) - ord('a')]
            result.add(morse_word)
        return len(result)

# Your runtime beats 78.24 % of python3 submissions.