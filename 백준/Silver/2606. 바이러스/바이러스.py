import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
adj_matrix = [[] for _ in range(N)]
counter = set()

for _ in range(M):
    A, B = map(int,input().split())
    adj_matrix[A-1].append(B)
    adj_matrix[B-1].append(A)


for i in adj_matrix[0]:
    counter.add(i)

pre_counter = set()

while pre_counter != counter:
    pre_counter = counter.copy()
    for i in pre_counter:
        for j in adj_matrix[i-1]:
            counter.add(j)
    
counter.discard(1)

print(len(counter))