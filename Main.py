class Node:
  def __init__(self, data,next):
    self.data = None
    self.next = None


class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, data) -> None:
      rear = self.rear
      node = Node(data)
      if(self.rear is None and self.front is None):
        self.rear , self.front = node , node
      else:
        self.rear.next = node
        self.rear = node

  def dequeue(self) -> None:
    if self.front is not None:
      self.front = self.front.next
    else:
      print("Queue is Empty")

    if self.rear.next is None:
      self.front = None
      self.rear = None

  def status(self) -> None:
    ptr = self.front
    while ptr:
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
