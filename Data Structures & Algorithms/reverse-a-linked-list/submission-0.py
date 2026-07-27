# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        a = []
        temp = head
        while temp:
            a.append(temp.val)
            temp = temp.next
        a = a[::-1]
        new = ListNode(a[0])
        temp = new
        for i in range(1,len(a)):
            temp.next = ListNode(a[i])
            temp = temp.next
        return new

        