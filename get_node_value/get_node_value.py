# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def get_node_value(head, index):
  count = 0
  curr = head
  
  while curr:
    if count == index:
      return curr.val
    else:
      curr = curr.next
      count += 1
  
  return None
​