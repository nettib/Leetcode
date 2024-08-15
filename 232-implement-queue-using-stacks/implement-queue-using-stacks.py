class MyQueue:

    def __init__(self):
        self.queue=MyQueue
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack1)!=0:
            self.stack2=self.stack1[::-1]
            temp=self.stack2[len(self.stack2)-1]
            self.stack2.pop()
            if len(self.stack2)!=0:
                self.stack1=self.stack2[::-1]
            else:
                self.stack1=[]
            return temp
        

    def peek(self) -> int:
        if len(self.stack1)!=0:
            self.stack2=self.stack1[::-1]
            return self.stack2[len(self.stack2)-1]

        

    def empty(self) -> bool:
        return len(self.stack1)==0
    
    
            
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()