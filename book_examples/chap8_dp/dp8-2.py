import sys

readline = sys.stdin.readline

if __name__ == '__main__':
    n = int(readline().rstrip())
    k = list(map(int, readline().rstrip().split()))
    d = [0] * n
    
    ### rsk's code
    # d[0], d[1] = k[0], k[1]

    # for i in range(2, n):
    #     d[i] = max(d[i-2], d[i-3]) + k[i]

    # print(max(d))

    ### ndb's code -> this code is better: no iteration at the end
    d[0] = k[0]
    d[1] = max(k[0], k[1])

    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2]+k[i])

    print(d[-1])
    