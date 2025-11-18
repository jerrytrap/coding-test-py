import sys
input = sys.stdin.readline

string = list(input().strip())
stack = []
answer = 0
temp = 1

for i, s in enumerate(string):
    if s == '(':
        stack.append(s)
        temp *= 2
    elif s == '[':
        stack.append(s)
        temp *= 3
    elif s == ')':
        # 짝이 안맞는 경우 0 출력
        if not stack or stack[-1] != '(':
            answer = 0
            break

        # () 모양인 경우에만 더해주기
        if string[i - 1] == '(':
            answer += temp

        stack.pop()
        temp //= 2
    elif s == ']':
        # 짝이 안맞는 경우 0 출력
        if not stack or stack[-1] != '[':
            answer = 0
            break

        # [] 모양인 경우에만 더해주기
        if string[i - 1] == '[':
            answer += temp

        stack.pop()
        temp //= 3

print(0 if stack else answer)
