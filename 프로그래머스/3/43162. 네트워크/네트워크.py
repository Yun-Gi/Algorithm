def solution(n, computers):
    answer = 1
    visit = [False] * n
    visit[0] = True
    for j in range(n):
        if not visit[j]:
            answer += 1
            visit[j] = True
            print(j, answer)

        queue = [j]
        while queue:
            a = queue.pop()
            for i in range(len(computers[a])):
                if computers[a][i] == 1 and not visit[i]:
                    visit[i] = True
                    queue.append(i)
        
         
    return answer


    