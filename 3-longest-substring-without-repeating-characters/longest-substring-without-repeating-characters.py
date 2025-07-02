class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_length = 0, 0
        sub = set()

        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1                
            sub.add(s[r])
            max_length = max(max_length, len(sub))    
        return max_length