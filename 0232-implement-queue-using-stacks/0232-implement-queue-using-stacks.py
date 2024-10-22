class MyQueue:

    def __init__(self):
        self.ip_stk = []
        self.op_stk = []

    def push(self, x: int) -> None:
        self.ip_stk.append(x)

    def pop(self) -> int:
        self.peek()
        return self.op_stk.pop()

    def peek(self) -> int:
        if not self.op_stk:
            while self.ip_stk:
                self.op_stk.append(self.ip_stk.pop())
        return self.op_stk[-1]

    def empty(self) -> bool:

        return not self.ip_stk and not self.op_stk


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
