# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alpha = list(string.ascii_lowercase)
        lookup = defaultdict(lambda:[])
        start = 0
        for n in range(2,10):
            if (n == 7 or n ==9):
                lookup[n] = alpha[start: start+4]
                start = start + 4
            else:
                lookup[n] = alpha[start: start+3]
                start = start + 3
                
        q = ['']
        ans = []
        comb = ''
        for i in digits:
            l = len(q)
            for j in range(l):
                for k in lookup[int(i)]:
                    comb = q[j]+k
                    if len(comb) == len(digits) :
                        ans.append(comb)
                    q. append(comb)
        return ans