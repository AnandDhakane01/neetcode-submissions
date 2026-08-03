
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p1 = head
        p2 = head.next

        p1.next = None
        while p2:
            nxt = p2.next
            p2.next = p1
            p1 = p2
            p2 = nxt
        return p1
