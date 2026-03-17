import sys
import heapq
input = sys.stdin.readline

n = int(input())
info = list(map(int, input().split()))
a = [(x, i) for i, x in enumerate(info)]
m = int(input())

heapq.heapify(a)

for _ in range(m):
    command = list(map(int, input().split()))

    if command[0] == 1:
        idx, v = command[1] - 1, command[2]

        # 1번 쿼리로 중간에 바뀌는 값은 info에서 관리
        info[idx] = v
        heapq.heappush(a, (info[idx], idx))
    elif command[0] == 2:
        while True:
            min_val, idx = a[0]

            # info가 갖고 있는 값이랑 같은지 비교, 아니라면 예전 값
            if info[idx] == min_val:
                print(idx + 1)
                break

            # 예전 값인 경우는 버려주기
            heapq.heappop(a)
