# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans=[]
        for l in lists:
            temp=l
            while temp:
                ans.append(temp.val)
                temp=temp.next
        ans.sort()
        dummy=ListNode()
        current=dummy
        for i in ans:
            current.next=ListNode(i)
            current=current.next
        return dummy.next
        
