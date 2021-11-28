# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head = result
        l1 = list1
        l2 = list2
        
        while l1 or l2:
            
            if (l2 is None) or (l1 and l1.val <= l2.val):
                val = l1.val
                l1 = l1.next
            elif (l1 is None) or (l2 and  l1.val > l2.val):
                val = l2.val
                l2 = l2.next
            
            result.next = ListNode(val)
            result = result.next
            
                
        return head.next