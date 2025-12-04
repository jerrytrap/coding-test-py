import sys
input = sys.stdin.readline

n = int(input())

answer = -1
for five in range(n // 5, -1, -1):
    remain = n - 5 * five
    if remain % 2 == 0:
        two = remain // 2
        answer = five + two
        break

print(answer)
