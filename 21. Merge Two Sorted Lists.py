# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        prev = None
        
        while(l1 != None and l2 != None):
            if(l1.val <= l2.val):
                if(head == None):
                    head = l1
                    prev = head
                else:
                    prev.next = l1
                    prev = l1
                l1 = l1.next
            else:
                if(head == None):
                    head = l2
                    prev = head
                else:
                    prev.next = l2
                    prev = l2
                l2 = l2.next
                    
        while(l1 != None):
            if(head == None):
                head = l1
                prev = head
            else:
                prev.next = l1
                prev = l1
            l1 = l1.next
        
        while(l2 != None):
            if(head == None):
                head = l2
                prev = head
            else:
                prev.next = l2
                prev = l2
            l2 = l2.next
        
        if(prev == None or head == None):
            return None
        
        prev.next = None
        return head

        
                
        
