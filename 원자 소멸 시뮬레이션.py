T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 원자의 개수 입력
    atoms = [list(map(int, input().split())) for _ in range(N)]
    # atoms 원소 형태: [x, y, 방향, 에너지]

    # 방향 정보
    # 문제 기준: 0 상, 1 하, 2 좌, 3 우
    delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    answer = 0  # 방출된 총 에너지 합

    # 0.5초 뒤 충돌까지 처리하기 위해 좌표를 2배로 확장
    # 예: (0,0) 과 (1,0)이 서로 마주보며 움직이면
    # 원래는 0.5초 뒤 충돌하지만,
    # 좌표를 2배 하면 정수 좌표에서 1초 단위처럼 처리 가능
    for i in range(N):
        atoms[i][0] *= 2
        atoms[i][1] *= 2

    # 최대 이동 가능 시간만큼 반복
    # 좌표 범위가 -1000 ~ 1000 이므로
    # 2배 확장 후 최대 범위는 -2000 ~ 2000
    # 끝에서 끝까지 이동해도 4000번이면 충분
    for _ in range(4000):

        # 원자가 1개 이하 남으면 더 이상 충돌 불가
        if len(atoms) <= 1:
            break

        # 이동 후 같은 위치에 모인 원자들을 저장할 딕셔너리
        # key   : (x, y)
        # value : 해당 위치에 있는 원자들 리스트
        pos_dict = {}

        # 모든 원자를 1칸씩 이동
        for atom in atoms:
            x, y, d, e = atom

            # 방향에 맞게 좌표 이동
            atom[0] += delta[d][0]
            atom[1] += delta[d][1]

            # 범위 밖으로 나간 원자는 더 이상 충돌할 일이 없으므로 버림
            if -2000 <= atom[0] <= 2000 and -2000 <= atom[1] <= 2000:
                pos = (atom[0], atom[1])

                # 해당 위치가 처음 나오면 빈 리스트 생성
                if pos not in pos_dict:
                    pos_dict[pos] = []

                # 이동한 원자를 그 위치 그룹에 추가
                pos_dict[pos].append(atom)

        # 다음 시간에 살아남을 원자들 저장
        new_atoms = []

        # 같은 위치에 모인 원자들 확인
        for pos, group in pos_dict.items():

            # 2개 이상이면 충돌 발생
            if len(group) >= 2:
                # 해당 위치 원자들의 에너지를 모두 더함
                for atom in group:
                    answer += atom[3]

            # 1개만 있으면 살아남음
            else:
                new_atoms.append(group[0])

        # 살아남은 원자만 다음 턴에 사용
        atoms = new_atoms

    print(f'#{tc} {answer}')