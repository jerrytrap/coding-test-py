import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
answer = 0
start = 1
end = k

while start <= end:
    mid = (start + end) // 2
    less = 0 # B의 원소 중 mid보다 작은 수의 개수

    for i in range(1, n + 1):
        less += min(mid // i, n)

    if less >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
