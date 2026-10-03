class MyStack:

    def __init__(self):
        #initialize a queue
        self.queue = deque()

    def push(self, x: int) -> None:
        #to push we just add to the queue using append
        self.queue.append(x) 

    def pop(self) -> int:
        #need to iterate through the queue then we need to add the left most element to the end of the element we want to remove
        for i in range(len(self.queue) - 1):
            #get the value of the left side of the queue then add it to the right of the element
        
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        #if the length of the queue is none zero
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()