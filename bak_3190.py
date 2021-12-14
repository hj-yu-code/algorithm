#### 아직못품
def solution():
    count = 0

    map_size = int(input())
    move = int(input())

    # 맵 구성
    map = [[0 for _ in range(map_size)] for _ in range(map_size)]
    for _ in range(move):
        x, y = map(int, input().split())
        map[x][y] = 1

    # 초기 머리, 꼬리 위치 설정
    hx, hy = 0, 0
    tx, ty = 0, 0

    # 방향 구성: 우, 하, 좌, 상
    view = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    Rot_count = int(input())
    for _ in range(Rot_count):
        time, rotate = input().split()

        for _ in range(time):
            count += 1
            # 위치 이동
            hx += dx[view]
            hy += dy[view]
            # tx += dx[view]
            # ty += dy[view]
            # 벽 탐지
            if hx<0 or hx>map_size or hy<0 or hy>map_size:
                return count
            # 꼬리 탐지
            if hx==tx and hy==ty:
                return count

            

        if rotate=="L":
            view -= 1
            if view < 0: view = 3 
        else:
            view += 1
            if view > 3: view = 0
            


if __name__ == '__main__':
    print(solution())
        


