import sys
from enum import Enum
input = sys.stdin.readline

class Color(Enum):
    WHITE = 0
    BLUE = 1

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
white_count = 0
blue_count = 0

def slice(paper, size):
    global white_count
    global blue_count

    if is_same_color(paper, Color.WHITE.value):
        white_count += 1
        return
    elif is_same_color(paper, Color.BLUE.value):
        blue_count += 1
        return
    else:
        slice([row[0:size//2] for row in paper[0:size//2]], size//2)
        slice([row[0:size//2] for row in paper[size//2:]], size//2)
        slice([row[size//2:] for row in paper[0:size//2]], size//2)
        slice([row[size//2:] for row in paper[size//2:]], size//2)

def is_same_color(paper, color):
    for i in range(len(paper)):
        for j in range(len(paper[0])):
            if paper[i][j] != color:
                return False
    return True

slice(info, n)
print(white_count)
print(blue_count)