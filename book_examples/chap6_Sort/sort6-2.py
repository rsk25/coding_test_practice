import sys

if __name__ == '__main__':
    nums = int(sys.stdin.readline().rstrip())
    student_score_table = []
    for _ in range(nums):
        student_info = sys.stdin.readline().split()
        student_info[-1] = int(student_info[-1])
        student_score_table.append(student_info)
    
    result = sorted(student_score_table, key=lambda x: x[-1])

    print(' '.join([name for name, _ in result]))
