
def turn(arr):
    return arr[1:N]+arr[0]



T = int(input())

for tc in range(1, 1+T):
    N, K = map(int, input().split())
    pwd = str(input())

    key = set()

    n = N // 4

    # 3번 진행
    for _ in range(n):
        # 순환 함수를 돌려서
        pwd = turn(pwd)
        # 4파트로 나눠서
        for i in range(4):
            # print(pwd[0:3])
            num_hex = pwd[i*n:n*(i+1)]
            # print(num_hex)
        # 16진수를 10진수로 변환해서 key에 넣기
            num = int(num_hex,16)
            key.add(num)
        # key를 정렬해서 k번째 값 찾기
    fin_key = sorted(key, reverse=True)
        # print(fin_key)

    ans = fin_key[K-1]
    print(f"#{tc} {ans}")