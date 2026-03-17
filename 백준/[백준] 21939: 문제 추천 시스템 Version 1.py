import sys
import heapq
input = sys.stdin.readline

n = int(input())
problems = dict()
min_heap = []
max_heap = []

def add(p, l):
    problems[p] = l
    heapq.heappush(min_heap, (l, p))
    heapq.heappush(max_heap, (-l, -p))

def recommend(x):
    if x == 1:
        while True:
            max_l, max_p = -max_heap[0][0], -max_heap[0][1]

            if max_p in problems and problems[max_p] == max_l:
                print(max_p)
                break

            heapq.heappop(max_heap)
    elif x == -1:
        while True:
            min_l, min_p = min_heap[0][0], min_heap[0][1]

            if min_p in problems and problems[min_p] == min_l:
                print(min_p)
                break

            heapq.heappop(min_heap)

def solved(p):
    del problems[p]

for _ in range(n):
    p, l = map(int, input().split())
    add(p, l)

m = int(input())

for _ in range(m):
    commands = input().split()
    command = commands[0]

    if command == "add":
        p, l = map(int, commands[1:])
        add(p, l)
    elif command == "recommend":
        x = int(commands[1])
        recommend(x)
    elif command == "solved":
        p = int(commands[1])
        solved(p)
