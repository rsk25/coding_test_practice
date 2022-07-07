import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())
    ls = []
    for i in range(n):
        ls.append(int(input().rstrip()))
    
    table = [m+1] * (m+1) # Goal number보다 큰 수를 '불가능'을 의미하도록 한다.
    table[0] = 0 # 0원을 만드는 경우도 고려해준다.
    # 화폐 단위 순서대로 table을 업데이트 한다.
    for i in range(n):
        for j in range(ls[i], m+1):
            table[j] = min(table[j], table[j-ls[i]]+1)
    
    if table[m] == m+1:
        print(-1)
    else:
        print(table[m])
