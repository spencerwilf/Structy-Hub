# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def sum_list(head):
  curr = head
  sum = 0
  
  while curr:
    sum += curr.val
    curr = curr.next
    
  return sum
​