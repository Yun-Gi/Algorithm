import sys
input = sys.stdin.readline

def jisho(meirei, jisho1):
    command, taisho = meirei.split()
    if command == 'insert':
        jisho1.add(taisho)
    else:
        if taisho in jisho1:
            print('yes')
        else:
            print('no')

n = int(input())
jisho1 = set() 
for _ in range(n):
    meirei = input().rstrip()
    jisho(meirei, jisho1)









           




