# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        result = ListNode()
        
        cur_r = result
        cur_l1 = l1
        cur_l2 = l2
        
        while 1:
            if cur_l1 is None:
                cur_l1 = ListNode()
            if cur_l2 is None:
                cur_l2 = ListNode()
                
            s = cur_l1.val + cur_l2.val + cur_r.val
            r = s % 10
            n = s / 10
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
            cur_r.val = r
            if cur_l1 or cur_l2 or n > 0:
                cur_r.next = ListNode(val=n)
                cur_r = cur_r.next
            else:
                break
            
        return result
            