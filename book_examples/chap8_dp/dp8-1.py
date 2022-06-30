import sys

reader = sys.stdin.readline

if __name__ == '__main__':
    x = int(reader().rstrip())
    # 앞서 계산된 결과를 저장하기 위한 DP-table 초기화
    d = [0] * (x+1)
    # Bottom-up
    # DP Table의 index가 숫자 역할을 한다.
    # DP Table의 value들은 각 index가 나타내는 숫자의 operation count을 기록하는 역할
    for i in range(2, x + 1):
        # 일단 무조건 현재 수에서 1을 뺀 경우부터 기록하는 이유: 
        # 모든 숫자는 일단 1을 빼는 행동은 유효한 operation이다.
        d[i] = d[i-1]+1
        # index가 나타내는 수가 나중에 2,3,5 중에서 나눠 떨어지는 것으로 판명되면, 
        # 그 이전에 (2|3|5)로 나누어 떨어졌던 수의 operation count를 이어받으면 된다.
        # 단, 이렇게 하는 것이 operation count가 더 적을 때만.
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    
    print(d[x])