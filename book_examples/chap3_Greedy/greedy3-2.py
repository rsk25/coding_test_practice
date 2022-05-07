import sys
from pathlib import Path
from typing import List


def sum_large_num(N: int, M: int, K: int, numbers: List[int]) -> int:
    numbers.sort()
    largest = numbers[N-1]
    second_largest = numbers[N-2]

    # 가장 큰 수가 더해지는 총 횟수
    cnt = int(M // K) * K
    cnt += M % (K+1) 

    result = 0
    result += cnt * largest # 가장 큰 수 더하기
    result += (M-cnt) * second_largest # 두 번째로 큰 수 더하기

    return result
    

if __name__ == '__main__':
    # set up
    lines = []
    with Path(f'./book_examples/chap3_Greedy/test/{sys.argv[1]}').open('r+t') as fp:
        for line in fp:
            lines.append(line)

    cmds = lines[0].split()
    N = int(cmds[0])
    M = int(cmds[1])
    K = int(cmds[2])
    numbers = [int(i) for i in lines[1].split()]

    large_num = sum_large_num(N, M, K, numbers)

    print(large_num)