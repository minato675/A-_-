T = int(input())

for tc in range(1, 1+T):
    N, M, K = map(int, input().split())
    
    tmp = [list(map(int, input().split())) for _ in range(N)]
    
    size = 650
    offset = 300
    
    life = [[0]*size for _ in range(size)]
    born = [[-1]*size for _ in range(size)]

    cells = []

    # 초기 배치
    for i in range(N):
        for j in range(M):
            if tmp[i][j] != 0:
                y = i + offset
                x = j + offset
                life[y][x] = tmp[i][j]
                born[y][x] = 0
                cells.append((y,x))

    
    
            
    
