

from tkinter import N


if __name__ == "__main__":
    coord = input()
    col = int(ord(coord[0])) - int(ord('a')) + 1
    row = int(coord[1])
    steps = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2), (2, 1), (1, 2)]

    # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
    result = 0
    for step in steps:
        next_row = row + step[0]
        next_col = col + step[1]
        if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
            result += 1
    
    print(result)