import sys

if __name__ == "__main__":
    n, k = map(int,sys.stdin.readline().rstrip().split())
    assert n >= k

    a = list(map(int,sys.stdin.readline().rstrip().split()))
    a.sort()
    b = list(map(int,sys.stdin.readline().rstrip().split()))
    b.sort(reverse=True)

    idx = 0
    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else: 
            break
    
    print(sum(a))
