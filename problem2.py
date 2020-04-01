# https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# Solution
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
  dummyHead = ListNode(0)
  l3 = dummyHead
  while l1 != None or l2 != None:
    if l2 == None:
      l3.next = ListNode(l1.val)
      l1 = l1.next
    elif l1 == None:
      l3.next = ListNode(l2.val)
      l2 = l2.next
    elif l1.val < l2.val:
      l3.next = ListNode(l1.val)
      l1 = l1.next
    else:
      l3.next = ListNode(l2.val)
      l2 = l2.next
    l3 = l3.next
  l3 = dummyHead.next
  return l3

# Testing
if __name__ == "__main__":
  l1 = ListNode(2)
  l1.next = ListNode(5)
  l1.next.next = ListNode(9)

  l2 = ListNode(1)
  l2.next = ListNode(9)
  l2.next.next = ListNode(23)

  l3 = mergeTwoLists(l1, l2)
  while l3 != None:
    print(f"{l3.val} ->", end="")
    if l3.next != None:
      l3 = l3.next
    else:
      break