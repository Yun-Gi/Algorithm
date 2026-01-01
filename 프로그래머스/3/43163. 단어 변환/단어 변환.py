from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [False] * len(words)
    queue = deque([(begin, 0)])
    
    while queue:
        current, depth = queue.popleft()
        if current == target:
            return depth
        for i in range(len(words)):
            if not visited[i] and can_change(current, words[i]):
                visited[i] = True
                queue.append((words[i], depth + 1))             
    return 0

def can_change(cur_word, next_word):
    diff_count = 0
    for a, b in zip(cur_word, next_word):
        if a != b:
            diff_count += 1
            
    return diff_count == 1
    