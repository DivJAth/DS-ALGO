# You are given an integer num. You can swap two digits at most once to get the maximum valued number.
# Return the maximum valued number you can get.
# Example 1:
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

# Example 2:
# Input: num = 9973
# Output: 9973
# Explanation: No swap.


class Solution:
    def maximumSwap(self, num: int) -> int:
        max_val = -float("inf")
        o_num = num
        hp, num = [],list(str(num))
        seen = set()
        for i in range(len(num) - 1, -1, -1):
            if num[i] not in seen:
                heapq.heappush(hp, (-int(num[i]),-i))
                seen.add(num[i])
        i = 0
        while hp:
            val, idx = heappop(hp)
            val = -1 * val
            idx = -1 * idx
            
            if i == idx:
                i += 1
            elif val > int(num[i]):
			    # swap places and encode the output
                num[i], num[idx] = num[idx], num[i]
                return int("".join(str(x) for x in num))
            else:
                heappush(hp, (-1 * val, -1 * idx))
                i += 1
        return o_num