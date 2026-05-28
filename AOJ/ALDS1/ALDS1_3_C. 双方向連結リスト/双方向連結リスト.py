import sys
input = sys.stdin.readline
from collections import deque

def doubleLinkedList(command, lst):
    if command == "deleteFirst":
        lst.popleft()
    elif command == "deleteLast":
        lst.pop()
    else:
        meirei, x = command.split()
        if meirei == "insert":
            lst.appendleft(x)
        elif meirei == "delete":
            try:
                lst.remove(x)
            except ValueError:
                pass

n = int(input())
lst = deque()
for _ in range(n):
    command = input().rstrip()
    doubleLinkedList(command, lst)
print(*lst)








           




