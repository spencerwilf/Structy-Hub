# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def is_univalue_list(head):
  
  curr = head
  val = head.val
  
  while curr:
    if curr.val != val:
      return False
    curr = curr.next
    
  return True
​