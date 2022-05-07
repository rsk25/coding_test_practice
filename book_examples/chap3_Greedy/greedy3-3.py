

if __name__ == '__main__':
    # setup
    n, m = map(int, input().split())
    result = 0

    for i in range(n):
        row = list(map(int, input().split()))
        min_num = min(row)
        result = max(result, min_num)
        
    print(result)
