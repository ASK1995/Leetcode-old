# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        count = 0
        
        head = None
        temp = None
        
        while(head1 != None and head2 != None):
            count += head1.val + head2.val
            if(head == None):
                head = ListNode(count % 10)
                temp = head
            else:
                x = ListNode(count % 10)
                temp.next = x
                temp = x
            count //= 10
            
            head1 = head1.next
            head2 = head2.next
        
        while(head1 != None):
            count += head1.val
            if(head == None):
                head = ListNode(count % 10)
                temp = head
            else:
                x = ListNode(count % 10)
                temp.next = x
                temp = x
            count //= 10
            head1 = head1.next
            
        while(head2 != None):
            count += head2.val
            if(head == None):
                head = ListNode(count % 10)
                temp = head
            else:
                x = ListNode(count % 10)
                temp.next = x
                temp = x
            count //= 10
            head2 = head2.next
        if(count != 0):
            x = ListNode(count)
            temp.next = x
            temp = x
        return head
            
