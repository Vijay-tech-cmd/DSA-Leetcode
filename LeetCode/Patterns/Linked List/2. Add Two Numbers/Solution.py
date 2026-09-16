# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        digits = []
        while l1:
            digits.append(l1.val)
            l1 = l1.next
        digits2 = []
        while l2:
            digits2.append(l2.val)
            l2 = l2.next
        num1 = int("".join(map(str, digits[::-1])))
        num2 = int("".join(map(str, digits2[::-1])))
        summ = num1 + num2
        result =  list(map(int, str(summ)))
        result.reverse()
        dummy = ListNode(0)
        current = dummy
        for digit in result:
            current.next = ListNode(digit)
            current = current.next
        return dummy.next