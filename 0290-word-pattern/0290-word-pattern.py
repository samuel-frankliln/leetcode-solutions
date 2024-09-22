class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = {}  # Dictionary to map words to pattern characters
        words = s.split()  # Split the string into words
        
        # If the number of words and pattern characters doesn't match, return False
        if len(words) != len(pattern):
            return False
        
        # Dictionary to map characters from the pattern to words
        pattern_map = {}
        
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            
            # If the character in the pattern is not in the map
            if char not in pattern_map:
                # If the word is already assigned to another character, return False
                if word in word_list:
                    return False
                # Assign the word to the character in the pattern
                pattern_map[char] = word
                word_list[word] = char
            else:
                # If the character exists, but the mapped word doesn't match the current word
                if pattern_map[char] != word:
                    return False
        
        return True
