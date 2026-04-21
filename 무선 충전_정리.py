def bfs(x,y,c,p,num):
    q = [[[x,y]]]
    head = 0
    dist = 0
    visited = [[0]*10 for _ in range(10)]
    charger.setdefault((x,y), []).append([p,num])
    visited[y][x] = 1

    while len(q)>head:
        #print(q)
        tmp = q[head] #[[x,y]]
        #print(tmp)
        for temp in tmp: # [x,y]
            #print(temp)
            row, col = temp
            same_dist_char = []
            # print(123213)
            # print(charger)
            for i in range(1, 5):
                nx, ny = row + d_x[i], col + d_y[i]
                if 0<=nx<10 and 0<=ny<10:
                    # print(ny)
                    if visited[ny][nx] == 0 and dist <= c :
                        charger.setdefault((nx,ny), []).append([p,num])
                        same_dist_char.append([nx,ny])
                        visited[ny][nx] = 1
                else:
                    continue
            q.append(same_dist_char)
        head += 1            
        dist += 1
    return


def charge(a,b):
    c_info_a = charger.get((a),[[0]])
    c_info_b = charger.get((b),[[0]])
    c_tmp = []
    if c_info_a != [[0]] and c_info_b != [[0]]:
        # print(c_info_a)
        for a_list in c_info_a:
            for b_list in c_info_b:
                # print(a_list)
                if a_list[1] == b_list[1]:
                    c_tmp.append(a_list[0])
                else:
                    c_tmp.append(a_list[0]+b_list[0])
    else:
        for a_list in c_info_a:
                for b_list in c_info_b:
                    c_tmp.append(a_list[0]+b_list[0])
    # print(c_tmp)
    return max(c_tmp)

T = int(input())

for tc in range(1, 1+T):
    M, A = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))
    info = [list(map(int, input().split())) for _ in range(A)]

    field = [[0]*10 for _ in range(10)] # 지도는 10*10 배열

    d_x = [0,0,1,0,-1] # 정지, 상, 우, 하, 좌
    d_y = [0,-1,0,1,0]

    charger = {}
    num = 0

    for c_x, c_y, c_c, c_p in info:
        num += 1
        bfs(c_x-1,c_y-1,c_c-1,c_p,num)

    # print(charger)
    a, b = (0,0), (9,9)
    ans = charge(a,b)
    # print(charge(a,b))
    for i in range(M):
        ord_a = move_a[i]
        ord_b = move_b[i]
        a = (a[0]+d_x[ord_a], a[1]+d_y[ord_a])
        b = (b[0]+d_x[ord_b], b[1]+d_y[ord_b])
        # print(a,b)
        ans += charge(a,b)
        # print(f'{i+1}번째 {charge(a,b)}')
        # print(ans)
    
    print(ans)
        




