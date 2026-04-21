T = int(input())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 반대 방향
reverse_dir = [1, 0, 3, 2]

# 블록에 따른 방향 전환
# 인덱스: 현재 방향(0상 1하 2좌 3우)
block_dir = {
    1: [1, 3, 0, 2],
    2: [3, 0, 1, 2],
    3: [2, 0, 3, 1],
    4: [1, 2, 3, 0],
    5: [1, 0, 3, 2]
}


def simulate(sx, sy, d, board, wormholes, N):
    x, y = sx, sy
    score = 0

    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        # 벽에 부딪힌 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            d = reverse_dir[d]
            score += 1
            x, y = nx, ny
            continue

        # 시작점으로 돌아오거나 블랙홀 만나면 종료
        if (nx, ny) == (sx, sy) or board[nx][ny] == -1:
            return score

        cell = board[nx][ny]

        # 빈칸
        if cell == 0:
            x, y = nx, ny

        # 블록
        elif 1 <= cell <= 5:
            d = block_dir[cell][d]
            score += 1
            x, y = nx, ny

        # 웜홀
        elif 6 <= cell <= 10:
            w1, w2 = wormholes[cell]
            if (nx, ny) == w1:
                x, y = w2
            else:
                x, y = w1

        # 혹시 다른 값이 있다면 그냥 이동
        else:
            x, y = nx, ny


for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 웜홀 위치 저장
    wormholes = {}
    for i in range(N):
        for j in range(N):
            if 6 <= board[i][j] <= 10:
                num = board[i][j]
                wormholes.setdefault(num, []).append((i, j))

    answer = 0

    # 모든 빈칸에서 4방향으로 출발
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for d in range(4):
                    answer = max(answer, simulate(i, j, d, board, wormholes, N))

    print(f"#{tc} {answer}")