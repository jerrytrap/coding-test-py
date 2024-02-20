import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken_buttons = list(input().split())
cur_channel = 100
answer = 1e9

def is_changeable(num):
    channel = str(num)

    for button in broken_buttons:
        if button in channel:
            return False

    return True

#채널 번호와 (+)(-) 버튼을 누르는 경우
for i in range(0, 1_000_001):
    if is_changeable(i):
        cnt = len(str(i)) + abs(n - i)
        answer = min(answer, cnt)

#현재 채널(100)에서 (+)(-) 버튼만 누르는 경우
answer = min(answer, abs(n - 100))

print(answer)