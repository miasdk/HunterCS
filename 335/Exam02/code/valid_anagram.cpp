#include <iostream>
#include <string>
#include <unordered_map>
class Solution {
    public:
        bool isAnagram(std::string s, std::string t) {
            if (s.length() != t.length()) return false; 
            std::unordered_map<char, int> freq; 
    
            for (char c : s) {
                freq[c]++;
            }
    
            for (char c : t){
                if (freq.find(c) == freq.end() || freq[c] == 0){
                    return false; 
                }
                freq[c]--;
            }
            return true; 
        }
    };

int main() {
    Solution solution;
    std::string s = "anagram";
    std::string t = "nagaram";
    
    if (solution.isAnagram(s, t)) {
        std::cout << s << " and " << t << " are anagrams." << std::endl;
    } else {
        std::cout << s << " and " << t << " are not anagrams." << std::endl;
    }
    
    return 0;
}
// Output:
// anagram and nagaram are anagrams.
