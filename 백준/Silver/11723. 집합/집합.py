import sys
input = sys.stdin.readline

class userSet:
    def __init__(self):
        self.set = set()
    
    def add(self, value):
        self.set.add(value)
    
    def remove(self, value):
        self.set.discard(value)
    
    def check(self, value):
        return value in self.set

    def toggle(self, value):
        if self.check(value):
            self.remove(value)
        else:
            self.add(value)
    
    def all(self):
        for i in range(1, 21):
            self.add(i)
    
    def empty(self):
        self.set.clear()


M = int(input())
userSet = userSet()

for _ in range(M):
    inputs = input().split()
    E = inputs[0]
    N = int(inputs[1]) if len(inputs) > 1 else None

    if E == "add":
        userSet.add(N)
    elif E == "remove":
        userSet.remove(N)
    elif E == "check":
        print(1 if userSet.check(N) else 0)
    elif E == "toggle":
        userSet.toggle(N)
    elif E == "all":
        userSet.all()
    elif E == "empty":
        userSet.empty()