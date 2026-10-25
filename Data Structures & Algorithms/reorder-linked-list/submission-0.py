# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        slow = fast = head 

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev= None 
        cur = slow 

        while cur:
            cur.next, prev, cur = prev,cur,cur.next

        first = head 
        second = prev

        while second.next:
            first.next, first = second, first.next
            second.next,second = first,second.next 

        