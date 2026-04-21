def bfs(x, y, c, p, num):
    q = [(x, y, 0)]   # (x좌표, y좌표, 거리)
    head = 0
    visited = [[0] * 10 for _ in range(10)]
    visited[y][x] = 1

    while len(q) > head:
        cx, cy, dist = q[head]
        head += 1

        charger.setdefault((cx, cy), []).append([p, num])

        if dist == c:
            continue

        for i in range(1, 5):
            nx = cx + d_x[i]
            ny = cy + d_y[i]

            if 0 <= nx < 10 and 0 <= ny < 10:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((nx, ny, dist + 1))


def charge(a, b):
    c_info_a = charger.get(a, [[0, -1]])
    c_info_b = charger.get(b, [[0, -1]])

    c_tmp = []

    for a_list in c_info_a:
        for b_list in c_info_b:
            if a_list[1] == b_list[1]:
                c_tmp.append(a_list[0])
            else:
                c_tmp.append(a_list[0] + b_list[0])

    return max(c_tmp)


T = int(input())

for tc in range(1, 1 + T):
    M, A = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))
    info = [list(map(int, input().split())) for _ in range(A)]

    d_x = [0, 0, 1, 0, -1]   # 정지, 상, 우, 하, 좌
    d_y = [0, -1, 0, 1, 0]

    charger = {}
    num = 0

    for c_x, c_y, c_c, c_p in info:
        num += 1
        bfs(c_x - 1, c_y - 1, c_c, c_p, num)

    a = (0, 0)
    b = (9, 9)

    ans = charge(a, b)

    for i in range(M):
        ord_a = move_a[i]
        ord_b = move_b[i]

        a = (a[0] + d_x[ord_a], a[1] + d_y[ord_a])
        b = (b[0] + d_x[ord_b], b[1] + d_y[ord_b])

        ans += charge(a, b)

    print(f'#{tc} {ans}')