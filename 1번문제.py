def sol1(n):
    tmp = 0
    start = N - n - 1
    for x in range(n + 1):
        if A[start + x] == B[x]:
            tmp += 1
    return tmp

def sol2(n):
    tmp = 0
    start = N - n - 1
    for x in range(n + 1):
        if A[x] == B[start + x]:
            tmp += 1
    return tmp



T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        val_1 = sol1(i)
        val_2 = sol2(i)
        ans = max(val_1, val_2, ans)

    print(f'#{tc} {ans}')