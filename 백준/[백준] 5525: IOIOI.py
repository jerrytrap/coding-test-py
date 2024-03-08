import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()
pattern_count = 0
answer = 0
i = 0

while i <= (m - 3):
    if s[i] == 'I' and s[i + 1] == 'O' and s[i + 2] == 'I':
        pattern_count += 1
        i += 2
        if pattern_count == n:
            pattern_count -= 1
            answer += 1
    else:
        pattern_count = 0
        i += 1

print(answer)
