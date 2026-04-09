import sys
input = sys.stdin.readline

N, M = map(int, input().split())
my_dict = {}

# 딕셔너리 생성
for i in range(N):
    my_dict[i+1] = []

# 그래프 생성
for _ in range(M):
    u, v = map(int, input().split())
    my_dict[u].append(v)
    my_dict[v].append(u)

visited = set()  # 방문기록용 집합
lst1 = [i+1 for i in range(N)]  # 1부터 전체 순회를 위한 스택
lst2 = []  # 깊이우선 탐색 전용 스택
counter = 0  # 결과값 구하는 카운터

while lst1:
    x = lst1.pop()
    if x not in visited:  # 방문 한 경우는 넘김
        lst2.append(x)
        counter += 1
    while lst2:
        y = lst2.pop()
        visited.add(y)  # y방문 완료
        for i in my_dict[y]:  # y와 연결되어 있고 방문하지 않은 노드들을 lst2에 삽입
            if i not in visited:
                lst2.append(i)

print(counter)