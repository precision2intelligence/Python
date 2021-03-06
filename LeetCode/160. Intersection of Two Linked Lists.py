#Time: O(m+n)
#Space: O(1)

# 统计两个链表的长度，去掉长列表的长度，然后遍历知道找到相同的节点
'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        m,n = self.GetLength(headA),self.GetLength(headB)
        if m > n:
            for i in range(m-n):
                headA = headA.next
            while headA != headB and headA and headB:
                headA = headA.next
                headB = headB.next
            return headA
        else:
            for i in range(n-m):
                headB = headB.next
            while headA != headB and headA and headB:
                headA = headA.next
                headB = headB.next
            return headA
    #统计链表长度
    def GetLength(self,pHead):
        if not pHead:
            return 0
        count = 0
        while pHead:
            pHead = pHead.next
            count += 1
        return count
