def copy(arr):
    # global H
    return [row[:] for row in arr]


def find_top(x, arr):
    for i in range(H):
        if arr[i][x] != 0:
            return i
    else:
        return -1

def cnt(arr):
    tmp = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                tmp += 1
    return tmp


def dfs(n, arr):
    global ans

    remain = cnt(arr)

    if remain == 0:
        ans = 0 
        return

    if n == N:
        ans = min(ans, remain)
        return
    
    for x in range(W):
           
        y = find_top(x,arr)
        
        if y == -1:
            dfs(n+1, arr)
            continue

        c_arr = copy(arr)
        explode(x, y, c_arr)
        c_arr = grav(c_arr)
        dfs(n+1,c_arr)

            

def grav(arr):
    n_arr = [[0]*W for _ in range(H)]
    for x in range(W):
        tmp = []
        
        for y in range(H-1, -1,-1):
            if arr[y][x] != 0:
                tmp.append(arr[y][x])

        
        for i in range(len(tmp)):
            n_arr[-i-1][x] = tmp[i]

    return n_arr

        

def explode(j,i,arr):

    if arr[i][j] == 0:
        return

    power = arr[i][j]
    arr[i][j] = 0
    delta = [[0,1],[0,-1],[1,0],[-1,0]]

    if power == 1:
        return

    for p in range(1,power):
        for dx, dy in delta:
            nx, ny = j+dx*p, i+dy*p

            if 0<=nx<W and 0<=ny<H:
                if arr[ny][nx] != 0:
                    explode(nx, ny, arr)
   
                    


                    
T = int(input()) # 문제 갯수

for tc in range(1, 1+T): # 테케 반복
    N, W, H = map(int, input().split()) # 떨어트릴 벽돌의 수, 가로(행), 세로(열)

    field = [list(map(int, input().split())) for _ in range(H)] # 필드 구현

    # print(field)

    ans = 99999999999999999999
    dfs(0,field)

    print(f'#{tc} {ans}')