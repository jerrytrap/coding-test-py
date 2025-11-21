import sys
input = sys.stdin.readline

number = input().strip()
n = len(number)

if number[0] == '0':
    print(0)
else:
    dp = [0 for _ in range(n)]
    dp[0] = 1

    for i in range(1, n):
        # i번째 수를 1자리로 해석하는 경우
        if number[i] != '0':
            dp[i] += dp[i - 1]

        # i번째 수를 2자리로 해석하는 경우
        two_digits = int(number[i - 1:i + 1])

        if 10 <= two_digits <= 26:
            if i == 1: # 0~1번째 수인 경우 1가지 밖에 없음
                dp[i] += 1
            else:
                dp[i] += dp[i - 2]

    print(dp[n - 1] % 1000000)
