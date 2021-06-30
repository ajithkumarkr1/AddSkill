class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        if l1.val < l2.val:
            return ListNode(l1.val,self.mergeTwoLists(l1.next,l2))
            
        else:
            return ListNode(l2.val,self.mergeTwoLists(l1,l2.next))
