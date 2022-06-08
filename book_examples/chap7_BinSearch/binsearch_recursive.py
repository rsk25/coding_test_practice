import sys
from typing import List


def recursive_binsearch(array: List[int], target: int, start_idx: int, end_idx: int):
    if start_idx > end_idx:
        return None
    mid_idx = (start_idx + end_idx) // 2
    if array[mid_idx] == target:
        return mid_idx
    elif array[mid_idx] > target:
        return recursive_binsearch(array, target, start_idx, mid_idx - 1)
    else:
        return recursive_binsearch(array, target, mid_idx + 1, end_idx)


if __name__ == "__main__":
    n, target = map(int, sys.stdin.readline().rstrip().split())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    start, end = 0, n - 1

    result = recursive_binsearch(array, target, start, end)

    if result is not None:
        print(result+1)
    else:
        print("Not found")

