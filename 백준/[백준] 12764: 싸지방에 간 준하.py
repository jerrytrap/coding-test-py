import sys
import heapq
from collections import Counter
input = sys.stdin.readline

n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
last_seat_number = 0 # 맨 마지막 자리 번호
used = [] # 컴퓨터를 사용한 자리 번호
computers = [] # 자리의 끝나는 시간을 저장
available_seats = [] # 앉을 수 있는 자리 후보

info.sort()

for p, q in info:
    # 현재 시작 시간 이전에 끝난 자리들을 앉을 수 있는 자리 목록에 넣어둠
    while computers and computers[0][0] <= p:
        _, seat_number = heapq.heappop(computers)
        heapq.heappush(available_seats, seat_number)

    # 앉을 수 있는 자리가 있다면 번호가 가장 작은 자리 선택
    if available_seats:
        seat_number = heapq.heappop(available_seats)
    # 앉을 수 있는 자리가 없다면 마지막 번호 +1 자리를 새로 만듦
    else:
        last_seat_number += 1
        seat_number = last_seat_number

    heapq.heappush(computers, (q, seat_number))
    used.append(seat_number)

counter = Counter(used)
print(last_seat_number)
print(" ".join(map(str, counter.values())))
