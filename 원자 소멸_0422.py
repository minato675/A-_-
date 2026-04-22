T = int(input())
for tc in range(1, 1 + T):
    N = int(input())

    delta = [[0, 1], [0, -1], [-1, 0], [1, 0]]  # 상 하 좌 우
    ans = 0

    atom_list = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        atom_list[i][0] *= 2
        atom_list[i][1] *= 2

    for _ in range(4000): # 4000 인 이유 극단적인 케이스 고려
        L = len(atom_list)
        if L <= 1:
            break

        inner_dict = {}

        # 1. 원자 이동 후 좌표별로 묶기
        for i_move in range(L):
            direction = atom_list[i_move][2]
            atom_list[i_move][0] += delta[direction][0]
            atom_list[i_move][1] += delta[direction][1]

            x, y = atom_list[i_move][0], atom_list[i_move][1]

            # 범위 안에 있는 원자만 저장
            if -2000 <= x <= 2000 and -2000 <= y <= 2000:
                pos = (x, y)
                inner_dict.setdefault(pos, []).append(atom_list[i_move])

        # 2. 충돌 처리
        live = []
        for pos, atoms in inner_dict.items():
            if len(atoms) >= 2:
                for atom in atoms:
                    ans += atom[3]
            else:
                live.append(atoms[0])

        atom_list = live

    print(f'#{tc} {ans}')