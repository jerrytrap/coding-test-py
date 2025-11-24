import sys
input = sys.stdin.readline

c = [0 for _ in range(31)]
c[0] = 1

for n in range(1, 31):
    total = 0
    for i in range(n):
        total += c[i] * c[n - 1 - i]
    c[n] = total

while True:
    n = int(input())
    if n == 0:
        break
    print(c[n])
