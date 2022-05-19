from collections import deque

def bfs(x, y, n, m, maze):
    queue = deque()
    queue.append((x,y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for d in zip(dx, dy):
            nx = x + d[0]
            ny = y + d[1]
            # 이동할 수 있는 노드가 아닌 경우 아무 행동하지 않는다
            if nx < 0 or nx >= n or ny < 0 or ny >= m or (maze[nx][ny] == 0):
                continue
            # 이동할 수 있는 노드라면 이전 노드 (x,y)의 값에 +1한 값을 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))

    return maze[n-1][m-1]


if __name__ == "__main__":
    n, m = map(int, input().split())

    maze = []
    for _ in range(n):
        maze.append(list(map(int, input())))
    
    print(bfs(0, 0, n, m, maze))
        