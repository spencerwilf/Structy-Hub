# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def reverse_list(head):
  
  prev = None
  curr = head
​
  while curr:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  return prev
    
    
    
# N <- a   b -> c -> d -> e -> f
# p    c   n