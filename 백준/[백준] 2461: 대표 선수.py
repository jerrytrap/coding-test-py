import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
classrooms = []
select = [] # (능력치, 학급 번호, 학생 순서)
max_ability = -1
answer = 10e9

for _ in range(n):
    classrooms.append(sorted(list(map(int, input().split()))))

# 각 반 별로 가장 낮은 점수부터 체크
for i in range(n):
    ability = classrooms[i][0]
    heapq.heappush(select, (ability, i, 0))
    max_ability = max(max_ability, ability)

while True:
    min_ability, class_number, idx = heapq.heappop(select)

    # 최대 - 최소 점수 갱신
    answer = min(answer, max_ability - min_ability)

    # 어떤 반의 마지막 학생까지 체크했다면 break
    if idx + 1 == m:
        break

    # 능력치가 가장 작은 학생이 있는 반의 다음 학생 능력치를 비교
    next_ability = classrooms[class_number][idx + 1]
    heapq.heappush(select, (next_ability, class_number, idx + 1))

    # 다음 학생 능력치가 최댓값일 수 있으므로 갱신
    max_ability = max(max_ability, next_ability)

print(answer)
