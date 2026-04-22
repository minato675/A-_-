    #DFS 진행 N< 발사횟수로 진행
# 남은 벽돌 세기
def cnt(arr):
    tmp = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                tmp += 1
    return tmp


#다중폭발 구현
def explode(j,i, arr):
    q = [(j,i)]
    head = 0
    delta = [[0,1],[0,-1],[1,0],[-1,0]]

    while len(q)>head:
        exp_x, exp_y = q[head]
        head += 1
        p = arr[exp_y][exp_x]
        arr[exp_y][exp_x] = 0

        for k in range(1,p):
            for dx, dy in delta:
                nx, ny = exp_x+(k*dx), exp_y+(k*dy)

                if 0<= nx < W and 0<= ny < H:
                    if arr[ny][nx] != 0:
                        q.append((nx,ny))


#투하지점 찾기
def find(x,arr):
    for y in range(H):
        if arr[y][x] != 0:
            return y
    return -1


#배열 복사
def copy(arr):
    return [row[:] for row in arr]

#중력적용
def grav(arr):
    new_field = [[0]*W for _ in range(H)]
    for x in range(W):
        tmp = []
        for y in range(H):
            y_reverse = -y-1
            if arr[y_reverse][x] != 0:
                tmp.append(arr[y_reverse][x])
        for i in range(len(tmp)):
            new_field[-i-1][x] = tmp[i]
    return new_field




# dfs 진행
def dfs(n, field):
    global ans
    remain = cnt(field)

    if remain == 0:
        ans = 0
        return

    if n == 0:
        ans = min(ans, remain)
        return
    
    for x in range(W):
        new_field = copy(field)

        y = find(x,new_field)


        if y == -1:
            dfs(n-1,new_field)

        explode(x,y,new_field)
        new_field = grav(new_field)
        dfs(n-1,new_field)




T = int(input())

for tc in range(1, 1+T):
    N, W, H = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(H)]
    ans = 999999999999999999

    dfs(N,board)

    print(f'#{tc} {ans}')