class MyQueue:

    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        # if not self._stack:
        return self._stack.pop(0) 

    def peek(self) -> int:
        return self._stack[0]

        
    def empty(self) -> bool:
        return len(self._stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()