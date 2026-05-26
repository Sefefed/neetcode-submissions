class MyCircularQueue:
  def __init__(self, k: int):
    self.myQueue = k * [None]
    self.start = -1
    self.rear = -1
    self.size = k
  def enQueue(self, value: int) -> bool:
    if self.isFull():
      return False
    else:
      if self.rear + 1 == self.size:
        self.rear = 0
      else:
        if self.start == -1:
          self.start = 0
        self.rear += 1  
      self.myQueue[self.rear] = value
      return True      
  def deQueue(self):
    if self.isEmpty():
      return False
    else:
      self.myQueue[self.start] = None
      if self.start == self.rear:
        self.start = -1
        self.rear = -1
      elif self.start + 1 == self.size:
        self.start = 0
      else:
        self.start += 1
      return True    
  def Front(self) -> int:
    if self.isEmpty():
      return -1
    else:
      return self.myQueue[self.start]
  def Rear(self) -> int:
    if self.isEmpty():
      return -1
    else:
      return self.myQueue[self.rear]
  def isEmpty(self) -> bool:
    if self.start == -1:
      return True
    else:
      return False
  def isFull(self) -> bool:
    if (self.rear + 1 == self.start) or (self.start == 0 and self.rear + 1 == self.size):
      return True
    else:
      return False      
            
      


        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()