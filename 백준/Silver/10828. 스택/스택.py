import sys

class stack:
    def __init__(self):
        self.arr = [None] * 10000
        self.pointer = -1

    def push(self, n:int):
        self.pointer += 1
        self.arr[self.pointer] = n

    def pop(self):
        if self.empty() == 0:
            N = self.arr[self.pointer]
            self.pointer -= 1
            return N
            
        else:
            return self.pointer

    def size(self):
        return self.pointer + 1

    def empty(self):
        if self.pointer == -1:
            return 1
        else:
            return 0

    def top(self):
        if self.empty() == 1:
            return -1
        else:
            return self.arr[self.pointer]


N = int(sys.stdin.readline().strip())
stack = stack()


for _ in range(N):
    inputs = sys.stdin.readline().strip().split()
    com = inputs[0]
    num = inputs[1] if len(inputs) > 1 else None

    if com == "push" and num is not None:
        stack.push(int(num))
    elif com == "pop":
        sys.stdout.write(str(stack.pop()) + "\n")
    elif com == "size":
        sys.stdout.write(str(stack.size()) + "\n")
    elif com == "empty":
        sys.stdout.write(str(stack.empty()) + "\n")
    elif com == "top":
        sys.stdout.write(str(stack.top()) + "\n")