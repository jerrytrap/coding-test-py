import sys
import heapq
input = sys.stdin.readline

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
classrooms = []

# 먼저 시작하는 강의부터 순차적으로 탐색
lectures.sort()

for s, t in lectures:
    # 가장 빨리 끝나는 강의실에 들어갈 수 있다면 그 강의실 사용
    if classrooms and classrooms[0] <= s:
        heapq.heappop(classrooms)

    # 새 강의실 사용 (빨리 끝나는 순서대로, 끝나는 시간만 기록)
    heapq.heappush(classrooms, t)

print(len(classrooms))
