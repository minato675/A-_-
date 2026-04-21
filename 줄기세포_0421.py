T = int(input())

for tc in range(1, 1+T):
    N, M, K = map(int,input().split())

    size = 700
    offset = 350

    field = [[0]*size for _ in range(size)]

    arr = [list(map(int, input().split())) for _ in range(N)]

    cell = []

    delta = [[0,1],[1,0],[0,-1],[-1,0]]
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                x, y = j+offset , i+offset
                t = life = arr[i][j]

                field[y][x] = 3
                cell.append([x,y,life,t,0])

    for _ in range(K):
        tmp  = {}
        for i in range(len(cell)): # x, y, life, time, state
            if cell[i][4] == 0:
                if cell[i][3] == 1:
                    cell[i][3] = cell[i][2]
                    cell[i][4] = 1
                else:
                    cell[i][3] -= 1
            
            else: # state 1인경우
                if cell[i][3] == cell[i][2]:
                    x, y = cell[i][0], cell[i][1]
                    for dx, dy in delta:
                        nx, ny = x+dx, y+dy
                        if field[ny][nx] ==0:
                            if (nx,ny) in tmp:
                                if tmp[(nx,ny)] < cell[i][2]:
                                    tmp[(nx,ny)] = cell[i][2]
                                else:
                                    continue
                            else:
                                tmp[(nx,ny)] = cell[i][2]
                    
                if cell[i][3] == 1:
                    # print(cell[i])
                    cell[i] = None
                    # print('ded')
                    
                else:
                    cell[i][3] -= 1
        new_cell = []
        for (a,b),l in tmp.items():
            field[b][a] = 3
            new_cell.append([a,b,l,l,0])
        
        for char in cell:
            if char is not None:
                new_cell.append(char)

        cell = new_cell

    ans = len(cell)
    # print(cell)
    print(f'#{tc} {ans}')                

                