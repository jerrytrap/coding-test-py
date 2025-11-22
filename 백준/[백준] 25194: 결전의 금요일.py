import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [False for _ in range(7)]
dp[0] = True # 월요일에서 시작

for i in a:
    after_work = i % 7
    new_dp = dp[:]

    for j in range(7):
        if dp[j]:
            new_dp[(j + after_work) % 7] = True

    dp = new_dp

if dp[4]:
    print('YES')
else:
    print('NO')
