# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        hp = []
        ## Remember!!
        ListNode.__eq__ = lambda self, other: self.val == other.val #define comparison method
        
        result = ListNode(0)
        head = result
        
        for l in  lists:
            if l:
                heapq.heappush(hp, (l.val, l))
        
        while hp:
            val, ele = heapq.heappop(hp)
            result.next = ListNode(val)
            result = result.next
            
            if ele.next:
                heapq.heappush(hp, (ele.next.val, ele.next) )
        
        return head.next
