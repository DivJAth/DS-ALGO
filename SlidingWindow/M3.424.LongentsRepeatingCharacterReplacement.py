# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        current_cnt = {}
        max_len, max_repeat = -float("inf"), -float("inf")
        while j < len(s):
            current_cnt[s[j]] = current_cnt.get(s[j], 0) + 1
            max_repeat = max(max_repeat, current_cnt[s[j]])
            if j-i+1 - max_repeat > k:
                current_cnt[s[i]] -=1
                i +=1
            max_len = max(max_len, j-i+1)
            
            j+=1
        return max_len