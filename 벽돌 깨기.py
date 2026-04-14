def count_bricks(board):
    cnt = 0
    for r in range(H):
        for c in range(W):
            if board[r][c] != 0:
                cnt += 1
    return cnt


def copy_board(board):
    return [row[:] for row in board]


def find_top(board, col):
    for r in range(H):
        if board[r][col] != 0:
            return r
    return -1


def explode(board, sr, sc): # sr, sc  폭발 시작 열 행
    # 큐를 리스트+head 방식으로 구현
    q = [(sr, sc, board[sr][sc])]
    head = 0
    board[sr][sc] = 0

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while head < len(q):
        r, c, power = q[head]
        head += 1

        # power가 1이면 자기 자신만 깨짐
        for d in range(4):
            for k in range(1, power):
                nr = r + dr[d] * k
                nc = c + dc[d] * k

                if not (0 <= nr < H and 0 <= nc < W):
                    break

                if board[nr][nc] == 0:
                    continue

                # 연쇄 폭발 대상이면 큐에 추가
                if board[nr][nc] > 1:
                    q.append((nr, nc, board[nr][nc]))

                # 어쨌든 벽돌은 제거
                board[nr][nc] = 0


def apply_gravity(board):
    for c in range(W):
        temp = []

        # 아래에서부터 벽돌 수집
        for r in range(H - 1, -1, -1):
            if board[r][c] != 0:
                temp.append(board[r][c])

        # 열 초기화
        for r in range(H):
            board[r][c] = 0

        # 아래부터 다시 채우기
        idx = H - 1
        for brick in temp:
            board[idx][c] = brick
            idx -= 1


def dfs(depth, board):
    global answer

    remain = count_bricks(board)
    if remain == 0:
        answer = 0
        return

    if depth == N: # 벽돌의 횟수 도달
        if remain < answer:
            answer = remain
        return

    # 이미 최적값이면 더 볼 필요 없음
    if answer == 0:
        return

    for c in range(W): # 모든 열에 대한 경우의수 계산 진행
        # 현재 맵 복사
        new_board = copy_board(board)

        top = find_top(new_board, c)

        # 해당 열에 벽돌이 없으면 변화 없이 다음 단계 (허공에 떨어트린 경우임)
        if top == -1:
            dfs(depth + 1, new_board)
            continue

        # 폭발 + 중력
        explode(new_board, top, c)
        apply_gravity(new_board)

        dfs(depth + 1, new_board)


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    answer = 999999999999999
    dfs(0, board)

    print(f'#{tc} {answer}')