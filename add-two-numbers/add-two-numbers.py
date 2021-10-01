# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        answer = head
        
        node1 = l1
        node2 = l2
        carry = 0
        
        while not (node1 == None and node2 == None and carry == 0):
            newnode = ListNode()
            if node1 == None:
                n1 = 0
            else:
                n1 = node1.val
            if node2 == None:
                n2 = 0
            else:
                n2 = node2.val
                
            if n1 + n2 + carry >= 10:
                
                newnode.val = ((n1+n2+carry)%10)
                carry = (n1 + n2 + carry) // 10
                head.next = newnode
            else:
                newnode.val = (n1+n2+carry)
                head.next = newnode
                carry=0
                
            head = head.next
            
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
        
        return answer.next
        