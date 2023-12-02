class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
​
def merge_lists(head_1, head_2):
  
  curr_1 = head_1
  curr_2 = head_2
  tail = Node(None)
  
  if head_1.val > head_2.val:
    tail.next = head_2
  else:
    tail.next = head_1
  
  while curr_1 and curr_2:
    
    if curr_1.val > curr_2.val:
      tail.next = curr_2
      curr_2 = curr_2.next
    else:
      tail.next = curr_1
      curr_1 = curr_1.next
    tail = tail.next
    
  if curr_1:
    tail.next = curr_1
  if curr_2:
    tail.next = curr_2
    
  if head_1.val > head_2.val:
    return head_2
  else:
    return head_1
     
​
  if curr_1: