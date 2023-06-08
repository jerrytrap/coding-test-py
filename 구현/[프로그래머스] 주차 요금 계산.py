import math


# 주차된 시간 계산
def cal_time(time_in, time_out):
    h_in, m_in = map(int, time_in.split(":"))
    h_out, m_out = map(int, time_out.split(":"))

    return (h_out * 60 + m_out) - (h_in * 60 + m_in)


def solution(fees, records):
    parking = {}  # 입차된 차 목록
    time = {}  # 주차한 시간
    answer = []

    for record in records:
        log = list(record.split(" "))

        # 입차인 경우
        if log[2] == 'IN':
            parking[log[1]] = log[0]
        # 출차인 경우
        else:
            parking_time = cal_time(parking[log[1]], log[0])
            if log[1] in time:
                time[log[1]] += parking_time
            else:
                time[log[1]] = parking_time

            del parking[log[1]]

    # 입차된 차가 나가지 않은 경우 23:59 출차로 계산
    for car in parking:
        parking_time = cal_time(parking[car], "23:59")
        if car in time:
            time[car] += parking_time
        else:
            time[car] = parking_time

    # 차량 번호를 기준으로 오름차순 정렬
    sorted_time = sorted(time.items())

    # 기본 시간을 기준으로 요금 계산
    for total_time in sorted_time:
        if total_time[1] < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((total_time[1] - fees[0]) / fees[2]) * fees[3])

    return answer