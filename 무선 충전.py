T = int(input())

for tc in range(1, 1+T):
    M, A = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))
    info = [list(map(int, input().split())) for _ in range(A)]

    field = [[0]*10 for _ in range(10)] # 지도는 10*10 배열

    
