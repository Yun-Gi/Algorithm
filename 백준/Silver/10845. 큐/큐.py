import sys

class Q:
    def __init__(self):
        self.arr = [None] * 10000
        self.inpointer = -1
        self.outpointer = 0

    def push(self, n:int):
        self.inpointer += 1
        self.arr[self.inpointer] = n

    def pop(self):
        if self.empty() == 0:
            N = self.arr[self.outpointer]
            self.outpointer += 1
            return N
              
        else:
            return -1

    def size(self):
        return self.inpointer - self.outpointer + 1

    def empty(self):
        if self.size() == 0 :
            return 1
        else:
            return 0

    def front(self):
        if self.empty() == 1:
            return -1
        else:
            return self.arr[self.outpointer]

    def back(self):
        if self.empty() == 1:
            return -1
        else:
            return self.arr[self.inpointer]

N = int(sys.stdin.readline().strip())
Q = Q()


for _ in range(N):
    inputs = sys.stdin.readline().strip().split()
    com = inputs[0]
    num = inputs[1] if len(inputs) > 1 else None

    if com == "push" and num is not None:
        Q.push(int(num))
    elif com == "pop":
        sys.stdout.write(str(Q.pop()) + "\n")
    elif com == "size":
        sys.stdout.write(str(Q.size()) + "\n")
    elif com == "empty":
        sys.stdout.write(str(Q.empty()) + "\n")
    elif com == "front":
        sys.stdout.write(str(Q.front()) + "\n")
    elif com == "back":
        sys.stdout.write(str(Q.back()) + "\n")