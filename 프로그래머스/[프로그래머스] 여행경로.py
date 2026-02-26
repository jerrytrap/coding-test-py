from collections import defaultdict

def solution(tickets):
    info = defaultdict(list) # 어떤 출발점에서 갈 수 있는 목적지들
    ticket_count = len(tickets)
    ticket_used = [False] * ticket_count # 티켓 사용 여부

    # 알파벳 순서가 앞서는 경로를 선택하기 위해 미리 정렬
    tickets.sort()

    def dfs(start, route, depth):
        if depth == ticket_count:
            return route

        # 어떤 출발점에서 사용할 수 있는 모든 티켓 체크
        for ticket_number, end in info[start]:
            if not ticket_used[ticket_number]:
                ticket_used[ticket_number] = True

                ans = dfs(end, route + [end], depth + 1)
                if ans:
                    return ans

                ticket_used[ticket_number] = False

        return None

    # 어떤 출발점에서 갈 수 있는 목적지를 티켓 번호와 함께 저장
    for ticket_number, (start, end) in enumerate(tickets):
        info[start].append((ticket_number, end))

    return dfs("ICN", ["ICN"], 0)
