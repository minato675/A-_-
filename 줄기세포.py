T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    OFFSET = 300
    SIZE = 650

    board = [[0] * SIZE for _ in range(SIZE)]
    q = []

    # 초기 세포 입력
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                y = i + OFFSET
                x = j + OFFSET
                life = arr[i][j]

                # (y, x, 생명력, 남은시간, 상태)
                # 상태: 0 비활성, 1 활성
                q.append((y, x, life, life, 0))
                board[y][x] = life

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # K시간 동안 반복
    for _ in range(K):
        new = {}  # 이번 시간 번식 결과

        size = len(q)

        for i in range(size):
            cell = q[i]
            if cell is None:
                continue

            y, x, life, timer, state = cell

            # 비활성 상태
            if state == 0:
                if timer == 1:
                    # 활성 상태로 전환
                    q[i] = (y, x, life, life, 1)
                else:
                    # 비활성 시간 감소
                    q[i] = (y, x, life, timer - 1, 0)

            # 활성 상태
            else:
                # 활성 시작 시 번식
                if timer == life:
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if board[ny][nx] != 0:
                            continue

                        if (ny, nx) in new:
                            if new[(ny, nx)] < life:
                                new[(ny, nx)] = life
                        else:
                            new[(ny, nx)] = life

                # 활성 종료 시 죽음
                if timer == 1:
                    q[i] = None
                else:
                    q[i] = (y, x, life, timer - 1, 1)

        # 번식 반영
        for (y, x), life in new.items():
            board[y][x] = life
            q.append((y, x, life, life, 0))

        # 죽은 세포 제거
        q = [cell for cell in q if cell is not None]

    print(f"#{tc} {len(q)}")