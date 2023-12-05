# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def longest_streak(head):
  
  if not head:
    return 0
  
  curr_streak = 1
  longest_streak = 0
  curr = head
  curr_val = None
  
  while curr:
    if curr.val == curr_val:
      curr_streak += 1
    else:
      curr_streak = 1
      curr_val = curr.val
    
    curr = curr.next
    longest_streak = max(curr_streak, longest_streak)
    
  return longest_streak
    
# 5 -> 5 -> 7 -> 7 -> 7 -> 6
#           ^