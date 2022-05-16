# 왼쪽으로 회전
def turn_left(direction):
   direction -= 1
   if direction == -1:
       direction = 3 


if __name__ == "__main__":
    n, m = map(int, input().split())

    # 방문한 위치를 저장하기 위한 맵을 생성
    d = [[0]*m for _ in range(n)]
    # 현재 캐릭터의 좌표와 방향
    x, y, direction = map(int, input().split())
    d[x][y] = 1 # 현재 좌표는 방문 처리

    # 전체 맵 정보를 입력받기
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))

    # 방향 설정
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 시뮬레이션 시작
    count = 1 # 최종 출력용
    turn_time = 0 # 모든 방향으로 다 봤는지 확인하기 위함
    while True:
        # 왼쪽으로 회전
        turn_left(direction)
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        else:
            turn_time += 1
        # 네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤로 갈 수 있다면 이동하기
            if array[nx][ny] == 0:
                x = nx
                y = ny
            # 뒤가 바다인 경우
            else:
                break
            turn_time = 0

    print(count)
