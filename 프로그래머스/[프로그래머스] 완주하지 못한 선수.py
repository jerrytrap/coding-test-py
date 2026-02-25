from collections import defaultdict

def solution(participant, completion):
    name_list = defaultdict(int)

    for p in participant:
        name_list[p] += 1

    for c in completion:
        name_list[c] -= 1

        if name_list[c] == 0:
            name_list.pop(c)

    return list(name_list.keys())[0]
