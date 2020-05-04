# https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. An integer is a 
# palindrome when it reads the same backward as forward.

def isPalindrome(x: int) -> bool:
  # TIME COMPLEXITY: O(logx) base 10
  str_x = str(x) # O(log(10)x)
  l = len(str_x) - 1 # O(1)
  for i in range(l): # O(log(10)x)
    if str_x[i] != str_x[l - i]: # O(1)
      return False  # O(1)
  return True