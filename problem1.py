# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# Solution:

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
  dummyNode = ListNode(0)
  l3 = dummyNode
  carry = 0
  while l1 != None or l2 != None:
    l1_val = l1.val if l1 != None else 0
    l2_val = l2.val if l2 != None else 0
    l3_sum = l1_val + l2_val + carry
    carry = l3_sum // 10
    print('carry', carry)
    l3_sum -= carry * 10
    l3.next = ListNode(l3_sum)
    # update l1, l2
    l1 = l1.next if l1 != None else l1
    l2 = l2.next if l2 != None else l2
    l3 = l3.next
  if carry > 0:
    l3.next = ListNode(1)
  l3 = dummyNode.next
  return l3


# Testing
if __name__ == "__main__":
  l1 = ListNode(2)
  l1.next = ListNode(4)
  l1.next.next = ListNode(3)

  l2 = ListNode(5)
  l2.next = ListNode(6)
  # l2.next.next = ListNode(4)

  l3 = addTwoNumbers(l1, l2)
  while l3 != None:
    print(f"{l3.val} ->", end="")
    if l3.next != None:
      l3 = l3.next
    else:
      break