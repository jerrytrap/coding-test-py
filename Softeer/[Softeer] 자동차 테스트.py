import sys
input = sys.stdin.readline

n, q = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def binary_search(num):
    start = 0
    end = len(data) - 1

    while start <= end:
        target = (start + end) // 2

        if data[target] == num:
            return target
        elif data[target] < num:
            start = target + 1
        else:
            end = target - 1

    return 0

for _ in range(q):
    m = int(input())
    smaller_nums = binary_search(m)
    greater_nums = len(data) - smaller_nums - 1
    print(smaller_nums * greater_nums)