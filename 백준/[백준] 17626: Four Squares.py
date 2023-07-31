from math import sqrt
from itertools import combinations_with_replacement

n = int(input())
square_num_1 = [i * i for i in range(1, int(sqrt(n)) + 1)] #제곱수
square_num_2 = [sum(i) for i in combinations_with_replacement(square_num_1, 2)] #두 제곱수의 합
square_num_3 = [sum(i) for i in combinations_with_replacement(square_num_1, 3)] #세 제곱수의 합

def solution(n):
    if n in square_num_1:
        return 1
    elif n in square_num_2:
        return 2
    elif n in square_num_3:
        return 3
    else:
        return 4

print(solution(n))