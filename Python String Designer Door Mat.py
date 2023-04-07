N, M = map(int, input().split())


c = 1
for i in range(N):
    if i == N // 2:
        print("WELCOME".center(M, '-'))
    elif i < N // 2:
        print((".|." * (c)).center(M, "-"))
        c += 2
    else:
        print((".|." * (c - 2)).center(M, "-"))
        c -= 2
