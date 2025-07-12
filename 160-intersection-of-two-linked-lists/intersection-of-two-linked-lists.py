# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if not headA or not headB:
            return None
        
        currA = headA
        currB = headB

        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
        
        return currA