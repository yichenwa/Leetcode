# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = 0
        c1 = 0
        while l1:
            n1 += (10 ** c1) * (l1.val)
            c1 += 1
            l1 = l1.next

        n2 = 0
        c2 = 0
        while l2:
            n2 += (10 ** c2) * (l2.val)
            c2 += 1
            l2 = l2.next

        sum = n1 + n2
        s = str(sum)
        s = s[::-1]
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for c in s:
            ptr.next = ListNode(int(c))
            ptr = ptr.next

        ptr = dummyRoot.next
        return ptr