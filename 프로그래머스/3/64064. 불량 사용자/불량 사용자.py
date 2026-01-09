def solution(user_id, banned_id):
    answer = 1
    lst = []
    for i in banned_id:
        temp = []
        for j in user_id:
            if len(i) == len(j):
                check = 1
                for k, l in zip(i,j):
                    if k != l and k != '*':
                        check = 0
                if check == 1:
                    temp.append(j)
        lst.append(temp)
    
    sett = set()
    
    def dfs(num, c_user):
        if num == len(banned_id):
            sett.add(tuple(sorted(c_user)))
            return
        for user in lst[num]:
            if user not in c_user:
                c_user.add(user)
                dfs(num+1, c_user)
                c_user.remove(user)
    
    dfs(0, set())
            
    return len(sett)