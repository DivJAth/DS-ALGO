# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"

# Example 2:

# Input: s = "aaab"
# Output: ""


class Solution:
    def reorganizeString(self, s: str) -> str:
        hp = []
        freq = {}
        
        for i in s:
            freq[i]= freq.get(i, 0) + 1
        
        for key in freq.keys():
            heapq.heappush(hp, (-freq[key],key))
        
        res = ""
        prev = heapq.heappop(hp)
        res += prev[1]
        
        while hp:
            curr = heapq.heappop(hp)
            res += curr[1]
            # Readd prev if it still has frequency left
            if prev[0] < -1:
                heapq.heappush(hp, (prev[0] + 1, prev[1]))
            prev = curr
        
        if len(res) != len(s):
            return ""
        return res
            
            
        