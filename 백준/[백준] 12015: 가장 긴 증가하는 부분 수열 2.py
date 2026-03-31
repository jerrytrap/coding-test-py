import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
lis = [a[0]]

for i in range(1, n):
    # LIS의 마지막 수보다 큰 경우 추가
    if a[i] > lis[-1]:
        lis.append(a[i])
    # LIS에 들어갈 위치를 찾아 바꿔주기
    else:
        idx = bisect_left(lis, a[i])
        lis[idx] = a[i]

print(len(lis))
