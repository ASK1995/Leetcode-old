# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        i1 = l1
        i2 = l2
        l3 = None
        head = None
        
        while(i1 != None and i2 != None):
            if(i1.val > i2.val):
                if(l3 == None):
                    l3 = i2
                    l3.val = i2.val
                    head = l3
                else:
                    x = i2
                    l3.next = x 
                    l3 = x
                i2 = i2.next
            else:
                if(l3 == None):
                    l3 = i1
                    l3.val = i1.val
                    head = l3
                else:
                    x = i1
                    l3.next = x 
                    l3 = x
                i1 = i1.next
        
        while(i1 != None):
            if(l3 == None):
                l3 = i1
                l3.val = i1.val
                head = l3
            else:
                x = i1
                l3.next = x 
                l3 = x 
            i1 = i1.next
        while(i2 != None):
            if(l3 == None):
                l3 = i2
                l3.val = i2.val
                head = l3
            else:
                x = i2
                l3.next = x 
                l3 = x 
            i2 = i2.next
        return head
