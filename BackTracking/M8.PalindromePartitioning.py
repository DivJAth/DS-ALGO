# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# A palindrome string is a string that reads the same backward as forward.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]
    
    def partionHelper(self, s, partition, ans):
        if not s:
            ans.append(partition[::])
            return
            
        for i in range(1, len(s)+1):
            prefix, postfix = s[:i], s[i:]
            if self.isPalindrome(prefix):
                partition.append(prefix)
                self.partionHelper(postfix, partition, ans)
                partition.pop()
            
            
    
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        partition = []
        self.partionHelper(s, partition, ans)
        return ans