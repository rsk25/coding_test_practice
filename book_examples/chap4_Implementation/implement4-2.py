
if __name__ == '__main__':
    n = input()
    upto_sixty = list(map(str, list(range(60))))

    cnt = 0
    for k in range(int(n)+1):
        if '3' in str(k):
            cnt += 3600
            continue
        for i in upto_sixty:
            if '3' in i:
                cnt += 60
                continue
            for j in upto_sixty:
                if '3' in j:
                    cnt += 1
    print(cnt)