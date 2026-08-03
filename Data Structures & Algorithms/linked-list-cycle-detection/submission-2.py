# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set() 
        p1 = head 

        while p1:
            if p1 in visited:
                return True
            visited.add(p1)
            p1 = p1.next

        return False




        