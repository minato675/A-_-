def cnt(arr):
    tmp = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                tmp += 1
    return tmp 

def find_top(j, arr):
    for i in range(H):
        if arr[i][j] != 0:
            return i
    
    return -1
    
def copy(arr):
    return [row[:] for row in arr]

def explode(x, y, arr):
    if arr[y][x] == 0:
        return
    power = arr[y][x]
    arr[y][x] = 0
    delta = [[1,0],[-1,0],[0,1],[0,-1]]
    for i in range(1,power):
        for dx, dy in delta:
            nx, ny = x+dx*i, y+dy*i

            if 0<=nx<W and 0<=ny<H:
                if arr[ny][nx] != 0:
                    explode(nx, ny, arr)
def grav(arr):
    n_arr = [[0]*W for _ in range(H)]
    for x in range(W):
        tmp = []
        for y in range(H-1,-1,-1):
            if arr[y][x] != 0:
                tmp.append(arr[y][x])
        
        for i in range(len(tmp)):
            n_arr[-i-1][x] = tmp[i]
    return n_arr



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

        c_arr = copy(arr)
        explode(x,y,c_arr)
        c_arr = grav(c_arr)
        dfs(n+1, c_arr)


T = int(input())

for tc in range(1, 1+T):
    N, W, H = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(H)]

    ans = 99999999999999999
    dfs(0,field)

    print(f"#{tc} {ans}")