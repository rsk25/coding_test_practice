import sys

input = sys.stdin.readline

def table_reset():
    table = [0] * n
    table[0] = 1
    table[1] = 3
    return table

if __name__ == "__main__":
    n = int(input().rstrip())
    table = [0] * n
    table[0] = 1
    table[1] = 3

    for i in range(2, n):
        table[i] = table[i-1] + table[i-1] - 1

    print(f"rsk: {table[-1]%796796}")

    table = table_reset()

    for i in range(2, n):
        table[i] = table[i-1] + table[i-2] * 2

    print(f"ndb: {table[-1]%796796}")