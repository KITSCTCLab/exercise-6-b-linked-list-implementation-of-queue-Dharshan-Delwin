class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
      last = self.last
      node = Node(data)
      if(self.last is None and self.head is None):
        self.last , self.head = node , node
      else:
        self.last.next = node
        self.last = node

  def dequeue(self) -> None:
    if self.head == self.last:
        self.head = self.last = None
    else:
        self.head = self.head.next

    

  def status(self) -> None:
    ptr = self.head
    while ptr != None:
      print(ptr.data,end = "=>")
      ptr = ptr.next
    print("None")


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
