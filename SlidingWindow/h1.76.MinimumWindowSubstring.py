# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
      
        if len(s) < len(t):
            return ""
               
        freq_t, freq_s  = {}, {}
        
        for i in t:
            freq_t[i] = freq_t.get(i, 0) + 1
        
        totCnt =len(freq_t)

        i, j, currCnt = 0, 0, 0
        min_dist = float('inf')
        
        while j < len(s):
            freq_s[s[j]] = freq_s.get(s[j],0) + 1
            
            if freq_t.get(s[j], 0) == freq_s[s[j]]:
                currCnt+=1
            
            while i <= j and currCnt == totCnt :
                if min_dist > j-i+1:
                    min_dist = j-i+1
                    i_min = i
                    j_min = j
                    
                freq_s[s[i]] -= 1
                if freq_s[s[i]] < freq_t.get(s[i],0):
                    currCnt-=1
                i+=1
            j+=1        
        
        return s[i_min: j_min+1] if min_dist != float('inf') else ""
