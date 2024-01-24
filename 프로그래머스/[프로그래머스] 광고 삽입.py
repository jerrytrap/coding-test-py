def convert_sec(time):
    hour, minute, second = map(int, time.split(':'))
    return hour * 3600 + minute * 60 + second

def convert_time(sec):
    second = sec % 60
    tmp = sec // 60
    hour = tmp // 60
    minute = tmp % 60

    return str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2)

def solution(play_time, adv_time, logs):
    play_time = convert_sec(play_time)
    adv_time = convert_sec(adv_time)
    watch_time = [0 for _ in range(play_time+1)]
    max_time = 0
    ans = 0

    #누적합을 위해 동영상 시작, 종료 지점 표시
    for log in logs:
        start, end = map(convert_sec, log.split('-'))
        watch_time[start] += 1
        watch_time[end] -= 1

    #누적합 1회 -> 재생된 동영상의 개수
    for i in range(1, play_time):
        watch_time[i] += watch_time[i-1]

    # 누적합 2회 -> 총 재생 시간
    for i in range(1, play_time):
        watch_time[i] += watch_time[i-1]

    #광고를 넣을 수 있는 모든 구간 체크
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            time = watch_time[i] - watch_time[i-adv_time]
        else:
            time = watch_time[i]

        if time > max_time:
            max_time = time
            ans = i-adv_time+1

    return convert_time(ans)
