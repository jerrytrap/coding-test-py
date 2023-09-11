import sys
input = sys.stdin.readline

n = int(input())
info = []
ans = 1

for _ in range(n):
    start, end = map(int, input().split())
    info.append((start, end))

info.sort(key= lambda x: (x[1], x[0]))

end = info[0][1]

for i in range(1, n):
    if info[i][0] >= end:
        end = info[i][1]
        ans += 1

print(ans)