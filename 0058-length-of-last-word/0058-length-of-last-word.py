class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string by spaces and filter out empty strings
        words = [word for word in s.split(" ") if word]
        # Return the length of the last word in the filtered list
        return len(words[-1]) if words else 0