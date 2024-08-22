class Solution {
public:
    bool canConstruct(std::string ransomNote, std::string magazine) {
        // Create a hashmap to store the frequencies of characters in the magazine
        std::unordered_map<char, int> magazine_map;

        // Populate the magazine_map with the character frequencies
        for (char c : magazine) {
            magazine_map[c]++;
        }

        // Check if all characters in ransomNote can be found in magazine_map with sufficient frequency
        for (char c : ransomNote) {
            // If the character is not found or its frequency is zero, return false
            if (magazine_map[c] == 0) {
                return false;
            }
            // Decrease the frequency of the character in magazine_map
            magazine_map[c]--;
        }

        // If all characters were found with sufficient frequency, return true
        return true;
    }
};