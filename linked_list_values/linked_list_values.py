# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def linked_list_values(head):
  curr = head
  res = []
  
  while curr:
    res.append(curr.val)
    curr = curr.next
  
  return res
​