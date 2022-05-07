

if __name__ == '__main__':
    # setup
    n, m = map(int, input().split())
    min_num = 0
    row_num = 0
    while row_num < n:
        row = map(int, input().split())
        _min = min(row)
        if min_num < _min:
            min_num = _min
        row_num += 1
    
    print(min_num)
