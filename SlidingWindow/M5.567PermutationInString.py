# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        s1_cnt = [0]*26
        s2_cnt = [0]*26
        
        for k in s1:
            s1_cnt[ord(k)-ord('a')]+=1
            
        while j < len(s2):
            s2_cnt[ord(s2[j])-ord('a')]+=1
            if s1_cnt == s2_cnt:
                return True
            
            while i<len(s2) and (j-i>=len(s1) or s2_cnt[ord(s2[i])-ord('a')]>s1_cnt[ord(s2[i])-ord('a')]):
                s2_cnt[ord(s2[i])-ord('a')]-=1
                i+=1
            j+=1
        return s1_cnt == s2_cnt