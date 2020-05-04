# https://leetcode.com/problems/reverse-integer/

# Given a 32-bit signed integer, reverse digits of an integer.

def reverse(self, x: int) -> int:
  # Time complexity: O(logk) base(10)
  if x > 2147483647 or x < -2147483648: # O(1)
    return 0
  str_x = list(str(x)) # O(logk) base10
  if str_x[0] == '-': del str_x[0] # O(1)
  l = len(str_x) - 1   # O(1)
  for i in range(len(str_x)//2):  # O(log k/2) base10
      str_x[i], str_x[l - i] = str_x[l - i], str_x[i]   # O(1)
  str_x = ''.join(str_x)  # O(logk) base 10
  return int(str_x) if x >= 0 else -1 * int(str_x)  # O(1)
