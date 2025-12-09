import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

n, m = len(s1), len(s2)
prev = [0 for _ in range(m + 1)]
cur = [0 for _ in range(m + 1)]
answer = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            cur[j] = prev[j - 1] + 1

            if cur[j] > answer:
                answer = cur[j]
        else:
            cur[j] = 0

    prev, cur = cur, prev

print(answer)
