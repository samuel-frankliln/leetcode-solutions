class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Hashmaps to store character frequencies
        ransom_hashmap = {}
        magazine_hashmap = {}

        # Populate the ransom_hashmap with the frequencies of characters in ransomNote
        for char in ransomNote:
            if char in ransom_hashmap:
                ransom_hashmap[char] += 1
            else:
                ransom_hashmap[char] = 1

        # Populate the magazine_hashmap with the frequencies of characters in magazine
        for char in magazine:
            if char in magazine_hashmap:
                magazine_hashmap[char] += 1
            else:
                magazine_hashmap[char] = 1

        # Check if the magazine can provide the characters needed for the ransom note
        for key, value in ransom_hashmap.items():
            if magazine_hashmap.get(key, 0) < value:
                return False

        return True
