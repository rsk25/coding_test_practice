
if __name__ == '__main__':
    nums = int(input())
    num_list = []
    for _ in range(nums):
        num_list.append(int(input()))

    num_list.sort(reverse=True)
    num_list_str = map(str, num_list)

    print(' '.join(num_list_str))