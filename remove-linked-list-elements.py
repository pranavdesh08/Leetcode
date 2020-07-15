# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        if head is None:
            return 
        
        cur = ListNode(0)
        cur.next = head
        head = cur
        
        if head is None:
            return []
        while cur.next != None:
            
            if cur is None:
                break
                
            elif cur.next.val == val:
               # node= ListNode(cur.val)
                cur.next = cur.next.next
            else:   
            
                cur = cur.next
            
        return head.next
                
