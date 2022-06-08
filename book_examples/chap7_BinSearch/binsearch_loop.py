import sys


def loop_binsearch(array, target, start_idx, end_idx):
    while True:
        if start_idx > end_idx:
            result = None
            break
        mid_idx = (start_idx + end_idx) // 2
        if array[mid_idx] == target:
            result = mid_idx
            break
        elif array[mid_idx] > target:
            end_idx = mid_idx - 1
        else:
            start_idx = mid_idx + 1 
    return result


if __name__ == "__main__":
    n, target = map(int,sys.stdin.readline().rstrip().split())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    start, end = 0, n - 1

    result = loop_binsearch(array, target, start, end)
    
    if result is not None:
        print(result+1)
    else:
        print("Not found")
