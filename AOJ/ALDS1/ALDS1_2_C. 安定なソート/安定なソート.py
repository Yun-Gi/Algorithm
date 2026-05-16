import sys
input = sys.stdin.readline

def selectionSort(A, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]

def bubbleSort(A, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if int(A[j][1]) < int(A[j-1][1]):
                A[j], A[j-1] = A[j-1], A[j]

N = int(input())
card = list(input().split())
card1 = card[:]

bubbleSort(card, N)
print(*card)
print("Stable")
selectionSort(card1, N)
print(*card1)
if card == card1:
    print("Stable")
else:
    print("Not stable")