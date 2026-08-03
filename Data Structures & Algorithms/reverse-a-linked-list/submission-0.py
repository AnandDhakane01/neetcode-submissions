
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p1 = head
        p2 = head.next
        p3 = None
        if p2:
            p3 = head.next.next


        p1.next = None
        while p2:
            p2.next = p1
            p1 = p2
            p2 = p3
            if p2:
                p3 = p2.next
        return p1
