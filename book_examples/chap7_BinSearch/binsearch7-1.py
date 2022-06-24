import sys

reader = sys.stdin.readline


def binsearch(array, target, start_idx, end_idx) -> bool:
    if start_idx > end_idx:
        return False
    mid_idx = (start_idx + end_idx) // 2
    if array[mid_idx] == target:
        return True
    elif array[mid_idx] > target:
        return binsearch(array, target, start_idx, mid_idx - 1)
    else:
        return binsearch(array, target, mid_idx + 1, end_idx)


if __name__ == "__main__":
    total_num = int(reader().rstrip())
    total_ls = sorted(list(map(int, reader().rstrip().split())))
    needed_num = int(reader().rstrip())
    needed_ls = sorted(list(map(int, reader().rstrip().split())))

    found_ls = []
    for needed in needed_ls:
        if binsearch(total_ls, needed, 0, total_num-1):
            found_ls.append('yes')
        else:
            found_ls.append('no')
    
    print(' '.join(found_ls))
