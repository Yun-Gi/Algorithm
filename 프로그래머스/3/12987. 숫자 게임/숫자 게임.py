def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A_index = 0
    B_index = 0
    for i in range(len(A)):
        if A[A_index] < B[B_index]:
            A_index += 1
            B_index += 1
            answer += 1
        else:
            B_index += 1
    return answer