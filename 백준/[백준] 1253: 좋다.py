import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
answer = 0

numbers.sort()

def check(idx, target):
    start = 0
    end = n - 1

    while start < end:
        # 자기 자신은 제외
        if start == idx:
            start += 1
            continue

        # 자기 자신은 제외
        if end == idx:
            end -= 1
            continue

        result = numbers[start] + numbers[end]

        if result < target:
            start += 1
        elif result > target:
            end -= 1
        else:
            return 1

    return 0

for idx, number in enumerate(numbers):
    answer += check(idx, number)

print(answer)
