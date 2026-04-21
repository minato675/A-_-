T = int(input())

delta = [[1,0],[0,-1],[-1,0],[0,1]]

block = {
    -1:[2,3,0,1],
    1:[2,3,1,0],
    2:[2,0,3,1],
    3:[3,2,0,1],
    4:[1,3,0,2],
    5:[2,3,0,1]
}

def sol(y, x, field, d, N):
    tmp_x, tmp_y = x, y
    score = 0

    while True:
        dx, dy = delta[d]
        nx, ny = x + dx, y + dy

        if tmp_x == nx and tmp_y == ny:
            return score

        if 0 <= nx < N and 0 <= ny < N:

            if field[ny][nx] == 0:
                x, y = nx, ny
                continue

            elif field[ny][nx] == -1:
                return score

            elif 1 <= field[ny][nx] <= 5:
                d = block[field[ny][nx]][d]
                score += 1
                x, y = nx, ny
                continue

            elif 6 <= field[ny][nx] <= 10:
                move = hole_dict[field[ny][nx]]
                for char in move:
                    if char != [nx, ny]:
                        x = char[0]
                        y = char[1]
                        break
                continue

        else:
            d = block[-1][d]
            score += 1
            x, y = nx, ny
            continue                         


for tc in range(1, 1+T):
    N = int(input()) # 가로 세로
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    hole_dict = {}
    for i in range(N):
        for j in range(N):
            if 6<=arr[i][j] :
                hole_dict.setdefault(arr[i][j],[]).append([j,i])


    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for k in range(4):
                    val = sol(i,j,arr,k,N)
                    ans = max(ans,val)
    
    print(f'#{tc} {ans}')







