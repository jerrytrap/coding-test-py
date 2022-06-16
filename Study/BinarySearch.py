# 이진 탐색
def binSearch(arr, findData):
    pos = -1
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if findData == arr[mid]:
            return mid
        elif findData > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return pos

