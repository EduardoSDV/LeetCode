class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

node1 = ListNode(val=0, next=None)
node2 = node1
print('node1 val', node1.val)
print('node1 next', node1.next)
print(id(node1), id(node2))
print("*****")

node3 = ListNode(val=3, next=None)
print('node1 val', node1.val)
print('node1 next', node1.next)
print(id(node1), id(node2))
print("*****")

node2.next = node3
node2 = node3
print('node1 val', node1.val)
print('node1 next', node1.next.val)
print(id(node1), id(node2))
print("*****")