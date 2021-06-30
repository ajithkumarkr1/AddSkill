class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.head = head
        current_node = self.head
        prev_node = None
        next_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        head = prev_node
        return head
