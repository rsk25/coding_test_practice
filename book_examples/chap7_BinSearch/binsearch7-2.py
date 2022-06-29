import sys
from functools import partial

read_line = sys.stdin.readline


def cut(num1, num2):
    result = num1 - num2
    if result <= 0:
        return 0
    else:
        return result

def get_len(func, ls):
    return sum(list(map(func, ls)))


def binsearch(item_lens: list, start_idx: int, end_idx: int, target_len: int):
    result = None
    while start_idx <= end_idx:
        mid = (start_idx + end_idx) // 2
        length = get_len(partial(cut, num2=mid), item_lens)
        if length < target_len:
            end_idx = mid - 1
        else:
            result = mid
            start_idx = mid + 1
    return result


if __name__ == '__main__':
    n, m = map(int, read_line().rstrip().split())
    items = list(map(int, read_line().rstrip().split()))
    result = binsearch(items, 0, max(items), m)
    if result is None:
        print("impossible!")
    print(result)
    