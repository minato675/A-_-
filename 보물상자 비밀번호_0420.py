def turn(arr,N):
    # print(arr)
    # print(arr[1:N], arr[0])
    return arr[1:N]+arr[0]

T = int(input())

for tc in range(1, 1+T):
    N, K = map(int, input().split())
    pw = str(input())
    pw_set = set()
    turn_ea = N // 4
    for i in range(turn_ea):
        for j in range(4):
            num_h = pw[turn_ea*j : turn_ea*(j+1)]
            # print(num_h)
            num_10 = int(num_h,16)
            pw_set.add(num_10)
        pw = turn(pw,N)
    pw_set = sorted(pw_set,reverse=True)
    ans = pw_set[K-1]
    print(f"#{tc} {ans}")

