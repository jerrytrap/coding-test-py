import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
size = 2 ** n
ans = 0
def visit(size, r, c):
    if size == 1:
        return
    global ans
    mid = size // 2

    #왼쪽 위
    if r < mid and c < mid:
        visit(mid, r, c)
    #오른쪽 위
    elif r < mid and c >= mid:
        ans += (size * size) // 4
        visit(mid, r, c - mid)
    #왼쪽 아래
    elif r >= mid and c < mid:
        ans += ((size * size) // 4) * 2
        visit(mid, r - mid, c)
    #오른쪽 아래
    else:
        ans += ((size * size) // 4) * 3
        visit(mid, r - mid, c - mid)

visit(size, r, c)
print(ans)