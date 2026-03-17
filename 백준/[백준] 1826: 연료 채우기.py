import sys
import heapq

input = sys.stdin.readline

n = int(input())
stations = [tuple(map(int, input().split())) for _ in range(n)]
l, p = map(int, input().split())

# 도착지 정보 미리 넣어두기
stations.append((l, 0))
stations.sort()

def solve(l, p):
    answer = 0
    heap = []

    for distance, amount in stations:
        # 다음 주유소까지 가는데 필요한 연료가 부족한경우
        while distance > p:
            # 주유소가 없는 경우 도착 불가능
            if not heap:
                print(-1)
                return

            # 연료를 가장 많이 넣을 수 있는 주유소 이용
            max_amount = -heapq.heappop(heap)
            p += max_amount
            answer += 1

        heapq.heappush(heap, -amount)

    print(answer)

solve(l, p)
