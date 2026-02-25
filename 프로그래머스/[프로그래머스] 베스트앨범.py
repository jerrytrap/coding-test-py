from collections import defaultdict

def solution(genres, plays):
    answer = []
    n = len(genres)
    play_count = defaultdict(int) # 장르별 총 재생 횟수
    playlist = defaultdict(list) # 어떤 장르에 해당하는 음악의 고유번호와 재생 횟수

    for i in range(n):
        play_count[genres[i]] += plays[i]
        playlist[genres[i]].append((i, plays[i]))

    # 많이 재생된 장르 순으로 정렬
    genres_ranking = [item[0] for item in sorted(play_count.items(), key=lambda x: x[1], reverse=True)]

    for genre in genres_ranking:
        # 장르 내에서 많이 재생된 순으로 정렬
        playlist[genre].sort(key=lambda x: x[1], reverse=True)

        # 최대 2개까지 추가
        for i in range(min(len(playlist[genre]), 2)):
            answer.append(playlist[genre][i][0])

    return answer
