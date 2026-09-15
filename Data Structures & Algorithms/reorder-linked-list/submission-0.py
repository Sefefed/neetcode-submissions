# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        cur = head
        n = len(stack)
        for i in range(n // 2):
            next_cur = cur.next
            last = stack.pop()
            cur.next = last
            last.next = next_cur
            cur = next_cur
        cur.next = None
            





