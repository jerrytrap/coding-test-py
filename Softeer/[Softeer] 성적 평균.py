import sys
input = sys.stdin.readline

n, k = map(int, input().split())
scores = list(map(int, input().split()))
prefix_sum = [0] + scores

for i in range(1, n + 1):
    prefix_sum[i] += prefix_sum[i - 1]

for _ in range(k):
    a, b = map(int, input().split())
    sum = prefix_sum[b] - prefix_sum[a - 1]
    avg = sum / (b - a + 1)
    print(f"{round(avg, 2):.2f}")