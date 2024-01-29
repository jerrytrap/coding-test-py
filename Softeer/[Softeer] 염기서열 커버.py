import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = []

for _ in range(n):
    dna.append(input())

super_dna = [None for _ in range(2**n)]
super_dna[0] = ['.'] * m

def merge(dna1, dna2):
    if dna1 == [] or dna2 == []:
        return []
    dna = []

    for i in range(m):
        if dna1[i] == '.':
            dna.append(dna2[i])
        elif dna2[i] == '.':
            dna.append(dna1[i])
        elif dna1[i] == dna2[i]:
            dna.append(dna1[i])
        else:
            return []
    return dna

def make_super_dna(index):
    loc = 0
    temp = index

    while temp % 2 == 0:
        temp //= 2
        loc += 1

    super_dna[index] = merge(dna[loc], super_dna[index-2**loc])

for i in range(1, 2**n):
    make_super_dna(i)

def calc_answer(index):
    if answer[index] < n+1:
        return answer[index]

    bit = []
    num1 = 0
    num2 = index
    temp_index = index

    for i in range(n):
        if temp_index % 2 == 1:
            bit.append(i)
        temp_index //= 2

    digit = [0] * len(bit)

    for i in range(1, 2**(len(bit)-1)):
        for j in range(len(bit)):
            if digit[j] == 1:
                digit[j] = 0
                temp = 2**bit[j]
                num1 -= temp
                num2 += temp
            else:
                digit[j] = 1
                temp = 2**bit[j]
                num1 += temp
                num2 -= temp
                break

        temp = calc_answer(num1) + calc_answer(num2)

        if answer[index] > temp:
            answer[index] = temp

    return answer[index]

answer = [n + 1 for _ in range(2 ** n)]
answer[0] = 0

for i in range(1, 2**n):
    if super_dna[i] != []:
        answer[i] = 1
    else:
        calc_answer(i)

print(answer[2**n-1])