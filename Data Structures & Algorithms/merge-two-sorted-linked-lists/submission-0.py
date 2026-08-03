# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode(-1000)
        new_list_p = new_list

        p1 = list1
        p2 = list2

        while p1 and p2:
            print(p1.val, p2.val)
            if p1.val >= p2.val:
                new_list_p.next = p2 
                p2 = p2.next
                new_list_p = new_list_p.next
            else: 
                new_list_p.next = p1 
                p1 = p1.next
                new_list_p = new_list_p.next

        if p1:
            new_list_p.next = p1
        
        if p2: 
            new_list_p.next = p2

        return new_list.next 


        