class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = op = ListNode(0)
        while head.next:
            if head.val != head.next.val:
                op.next = head
                op = op.next
            head = head.next
        op.next = head
        return dummy.next