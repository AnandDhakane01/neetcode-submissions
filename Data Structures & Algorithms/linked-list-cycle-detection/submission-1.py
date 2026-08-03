# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        p1 = head 

        while p1:
            if p1 in hashmap:
                return True
            hashmap[p1] = 1
            p1 = p1.next

        return False




        