import sys

input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
answer = 0

houses.sort()

start = 1 # 공유기 사이 최소 거리
end = houses[-1] - houses[0] # 공유기 사이 최대 거리

while start <= end:
    mid = (start + end) // 2

    # 첫 번째 집부터 시작
    cur = houses[0]
    count = 1

    # 공유기 사이 거리가 mid 이상인 경우 설치
    for i in range(1, n):
        if houses[i] >= cur + mid:
            cur = houses[i]
            count += 1

    # 공유기를 C개보다 많이 설치할 수 있다면 간격을 늘려보기
    if count >= c:
        answer = mid
        start = mid + 1
    # C개를 설치할 수 없다면 간격을 좁혀보기
    else:
        end = mid - 1

print(answer)
