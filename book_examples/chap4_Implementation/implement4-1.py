

if __name__ == '__main__':
    n = int(input())
    cmd = list(input().split())
    start = [1, 1]

    for c in cmd:
        if c == 'R':
            start[1] += 1
            if start[1] > n:
                start[1] -= 1
        elif c == 'L':
            start[1] -= 1
            if start[1] <= 0:
                start[1] += 1
        elif c == 'U':
            start[0] -= 1
            if start[0] <= 0:
                start[0] += 1
        else:
            start[0] += 1
            if start[0] > n:
                start[0] -= 1
    
    print(start[0], start[1])
    