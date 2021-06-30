class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        l=[]
        if head is None:
            return
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        l.sort()
        temp=head
        i=0
        while temp:
            temp.val=l[i]
            i+=1
            temp=temp.next
        return head
