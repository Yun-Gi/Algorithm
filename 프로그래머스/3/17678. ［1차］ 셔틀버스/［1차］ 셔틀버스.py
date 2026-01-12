def solution(n, t, m, timetable):
    time = sorted([int(t[:2])*60 + int(t[3:]) for t in timetable])
    busTime = [540 + i*t for i in range(n)]
    idx = 0
    for i in busTime:
        cnt = 0
        while cnt < m and idx < len(time) and time[idx] <= i:
            idx += 1
            cnt += 1
        if i == busTime[-1]:
            if cnt < m:
                return minutes_to_str(i)
            else:
                return minutes_to_str(time[idx-1] - 1)

def minutes_to_str(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"