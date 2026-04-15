T = int(input())

for tc in range(1, 1+T):
    N = int(input()) # 원자들의 수
    atom = []
    for i in range(N):
        x, y, d, e = map(int,input().split()) # 좌표와 방향 에너지
        atom.append([x*2,y*2,d,e])
    delta = [[0,1],[0,-1],[-1,0],[1,0]] # 상 하 좌 우
    eng = 0
    for t in range(4000):
        tmp = set()
        if len(atom) <= 1:
            break
        for i in range(len(atom)):
            atom[i][0] += delta[atom[i][2]][0]
            atom[i][1] += delta[atom[i][2]][1]
            if atom[i][0] >2000 or atom[i][0] < -2000 or atom[i][1] > 2000 or atom[i][1]< -2000:
                tmp.add(i)

        for i in range(len(atom)):
            for j in range(len(atom)):
                if i != j and atom[i][0] == atom[j][0] and atom[i][1]==atom[j][1]:
                    eng += atom[i][3] + atom[j][3]
                    atom[i][3] = atom[j][3] = 0
                    tmp.add(i)
                    tmp.add(j)

        for num in sorted(tmp, reverse=True):
            atom.pop(num)
    print(f'#{tc} {eng}')
        

