T = int(input())

for tc in range(1, 1+T):
    N, K = map(int, input().split())
    arr = str(input())
    ans = set()
    F = N // 4
    for _ in range(F):
        k = 1
        k %= len(arr)
        arr = arr[-k:] + arr[:-k]
        for i in range(4):
            h = arr[F*i:F*(i+1)]
            # print(h)
            tmp = int(h,16)
            ans.add(tmp)
    ans = sorted(ans, reverse=True)
    # print(ans)
    print(f'#{tc} {ans[K-1]}')